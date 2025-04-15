
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    parent_id INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL UNIQUE,
    author VARCHAR(100) NOT NULL,
    category_id INT DEFAULT 0,
    description TEXT,
    cover_url VARCHAR(255),
    status VARCHAR(20) DEFAULT '连载中',
    total_chapters INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS chapters (
    chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INT NOT NULL,
    chapter_name VARCHAR(100) NOT NULL,
    chapter_order INT NOT NULL,
    word_count INT DEFAULT 0,
    published_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS contents (
    content_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INT NOT NULL,
    page_number INT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id) ON DELETE CASCADE
);

-- 索引定义单独作为CREATE INDEX语句
CREATE INDEX IF NOT EXISTS idx_books_title ON books(title);
CREATE INDEX IF NOT EXISTS idx_books_author ON books(author);
CREATE INDEX IF NOT EXISTS idx_books_category ON books(category_id);
CREATE INDEX IF NOT EXISTS idx_chapters_book ON chapters(book_id, chapter_order);
CREATE INDEX IF NOT EXISTS idx_contents_chapter_page ON contents(chapter_id, page_number);