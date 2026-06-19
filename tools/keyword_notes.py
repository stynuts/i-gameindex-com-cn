from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# 示例网站与关键词配置（仅用于演示数据组织）
SAMPLE_SITE = "https://i-gameindex.com.cn"
SAMPLE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """使用 dataclass 表示一条关键词笔记"""
    keyword: str
    source_url: str
    note: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def short_summary(self, max_len: int = 50) -> str:
        """返回简短的笔记摘要"""
        if len(self.note) <= max_len:
            return self.note
        return self.note[:max_len] + "…"


def format_note_as_text(note: KeywordNote) -> str:
    """将一条 KeywordNote 格式化为可读文本"""
    lines = [
        f"关键词：{note.keyword}",
        f"来源：{note.source_url}",
        f"时间：{note.created_at}",
        f"标签：{', '.join(note.tags) if note.tags else '无'}",
        f"笔记：{note.note}",
        "—" * 30,
    ]
    return "\n".join(lines)


def format_notes_as_table(notes: List[KeywordNote]) -> str:
    """将多条笔记格式化为表格样式的字符串（简易文本表格）"""
    if not notes:
        return "（无笔记）"
    header = f"{'关键词':<10} {'来源':<30} {'标签':<20} {'笔记摘要':<40}"
    sep = "-" * len(header)
    rows = [header, sep]
    for n in notes:
        keyword = n.keyword if len(n.keyword) <= 8 else n.keyword[:8] + "…"
        url = n.source_url if len(n.source_url) <= 28 else n.source_url[:28] + "…"
        tags = ", ".join(n.tags) if n.tags else "—"
        summary = n.short_summary(36)
        rows.append(f"{keyword:<10} {url:<30} {tags:<20} {summary:<40}")
    return "\n".join(rows)


def generate_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记，供演示或测试使用"""
    notes = [
        KeywordNote(
            keyword=SAMPLE_KEYWORD,
            source_url=SAMPLE_SITE,
            note="爱游戏是一个专注于游戏资讯与测评的中文站点，内容覆盖全平台。",
            tags=["游戏", "资讯", "中文"],
        ),
        KeywordNote(
            keyword="独立游戏",
            source_url=SAMPLE_SITE,
            note="该网站收录了大量独立游戏推荐及开发访谈，适合开发者社区。",
            tags=["独立", "开发者", "推荐"],
        ),
        KeywordNote(
            keyword="游戏测评",
            source_url=SAMPLE_SITE,
            note="测评文章由资深玩家撰写，视角独特且评分标准透明。",
            tags=["测评", "深度"],
        ),
    ]
    return notes


def demo_keyword_notes():
    """演示 KeywordNote 的创建与格式化输出"""
    sample_notes = generate_sample_notes()

    print("=== 单条笔记文本格式 ===")
    print(format_note_as_text(sample_notes[0]))
    print()

    print("=== 多条笔记表格格式 ===")
    print(format_notes_as_table(sample_notes))


if __name__ == "__main__":
    demo_keyword_notes()