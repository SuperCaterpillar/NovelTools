from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50), nullable=False, unique=True)
    parent_id = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())

    # 定义反向关系
    books = relationship("Book", back_populates="category")


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, unique=True)
    author = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), default=0)
    description = Column(Text)
    cover_url = Column(String(255))
    status = Column(String(20), default="连载中")
    total_chapters = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # 定义关系
    category = relationship("Category", back_populates="books")
    chapters = relationship(
        "Chapter", back_populates="book", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_books_title", "title"),
        Index("idx_books_author", "author"),
        Index("idx_books_category", "category_id"),
    )


class Chapter(Base):
    __tablename__ = "chapters"

    chapter_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(
        Integer, ForeignKey("books.book_id", ondelete="CASCADE"), nullable=False
    )
    chapter_name = Column(String(100), nullable=False)
    chapter_order = Column(Integer, nullable=False)
    word_count = Column(Integer, default=0)
    published_at = Column(DateTime, default=func.now())

    # 定义关系
    book = relationship("Book", back_populates="chapters")
    contents = relationship(
        "Content", back_populates="chapter", cascade="all, delete-orphan"
    )

    __table_args__ = (Index("idx_chapters_book", "book_id", "chapter_order"),)


class Content(Base):
    __tablename__ = "contents"

    content_id = Column(Integer, primary_key=True, autoincrement=True)
    chapter_id = Column(
        Integer, ForeignKey("chapters.chapter_id", ondelete="CASCADE"), nullable=False
    )
    page_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())

    # 定义关系
    chapter = relationship("Chapter", back_populates="contents")

    __table_args__ = (Index("idx_contents_chapter_page", "chapter_id", "page_number"),)


# 创建表结构
def create_tables(engine):
    Base.metadata.create_all(engine)


class NovelDBManager:
    def __init__(self, url: str, echo=False):
        self.engine = create_engine(url, echo=echo)
        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        # session = Session()

    def add_book(self, title, author, category_id, description, cover_url, status):
        with self.Session() as session:  # 使用上下文管理器
            try:
                existing = session.query(Book).filter_by(title=title).first()
                if existing:
                    print(f"书籍 '{title}' 已存在，跳过插入")
                    return existing
                new_book = Book(
                    title=title,
                    author=author,
                    category_id=category_id,
                    description=description,
                    cover_url=cover_url,
                    status=status,
                )
                session.add(new_book)
                session.commit()
            except Exception as e:
                session.rollback()

    def add_chapter(self, book_id, chapter_name, chapter_order, word_count):
        with self.Session() as session:  # 使用上下文管理器
            try:
                existing = (
                    session.query(Chapter)
                    .filter_by(book_id=book_id, chapter_name=chapter_name)
                    .first()
                )
                if existing:
                    print(f"书籍 {book_id} 的章节 '{chapter_name}' 已存在，跳过插入")
                    return existing

                new_chapter = Chapter(
                    book_id=book_id,
                    chapter_name=chapter_name,
                    chapter_order=chapter_order,
                    word_count=word_count,
                )
                session.add(new_chapter)
                session.commit()

            except Exception as e:
                session.rollback()

    def add_content(self, chapter_id, page_number, content):
        with self.Session() as session:  # 使用上下文管理器
            try:
                existing = (
                    session.query(Content)
                    .filter_by(chapter_id=chapter_id, page_number=page_number)
                    .first()
                )
                if existing:
                    print(f"章节 {chapter_id} 的第 {page_number} 页已存在，跳过插入")
                    return existing
                new_content = Content(
                    chapter_id=chapter_id, page_number=page_number, content=content
                )
                session.add(new_content)
                session.commit()

            except Exception as e:
                session.rollback()

    def add_category(self, category_name, parent_id=0):
        with self.Session() as session:  # 使用上下文管理器
            try:
                existing = (
                    session.query(Category)
                    .filter_by(category_name=category_name)
                    .first()
                )
                if existing:
                    print(f"分类 '{category_name}' 已存在，跳过插入")
                    return existing  # 返回现有记录
                new_category = Category(
                    category_name=category_name, parent_id=parent_id
                )
                session.add(new_category)
                session.commit()
            except Exception as e:
                session.rollback()


if __name__ == "__main__":

    manager = NovelDBManager("sqlite:///db/test.db", echo=True)

    manager.add_category("小说")
    manager.add_category("科幻")
    manager.add_category("武侠")
    manager.add_category("都市")
    manager.add_category("历史")
    manager.add_category("游戏")

    manager.add_book(
        title="Python编程实战",
        author="张三",
        category_id=1,
        description="一本Python编程书籍",
        cover_url="http://example.com/cover.jpg",
        status="已完结",
    )

    manager.add_book(
        title="Python编程实战",
        author="李四",
        category_id=1,
        description="重复书籍测试",
        cover_url="http://example.com/cover2.jpg",
        status="连载中",
    )
    # # 示例操作

    # # 示例

    # # 示例操作
    # new_category = Category(category_name="小说")
    # session.add(new_category)
    # session.commit()

    # new_book = Book(
    #     title="Python编程实战",
    #     author="张三",
    #     category=new_category,
    #     description="一本Python编程书籍"
    # )
    # session.add(new_book)
    # session.commit()

    # book = session.query(Book).first()
    # print(book.category)  # 通过 relationship 访问
