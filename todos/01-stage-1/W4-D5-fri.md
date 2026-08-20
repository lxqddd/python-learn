# W4 D5 周五 · 4h — 综合 Python CLI 工具

- **阶段**：1 Python 强化 | **周次**：W4 | **状态**：⬜
- **主题**：完整 CLI 项目，巩固 Python 工程能力

---

## 🎯 今日目标（1 项）

- [ ] **完成 `sandbox/tiny-projects/03-file-manager/` 综合 CLI 工具**

---

## ✅ 任务清单（4h）

### 💻 项目设计（30min）

- [ ] **[30min]** 项目需求：

  ```markdown
  # File Manager CLI
  
  ## 功能
  - 搜索文件名（支持 glob 模式）
  - 统计目录大小
  - 查找重复文件
  - 按修改时间排序
  - 批量重命名
  - 导出 JSON 报告
  
  ## 技术栈
  - argparse（CLI 参数）
  - pathlib（文件操作）
  - pydantic（配置 + 数据模型）
  - python-dotenv（配置）
  - rich（漂亮打印）
  - pytest（测试）
  
  ## 验收
  - ≥ 5 个子命令
  - 每个命令支持 --help
  - 至少 5 条 pytest 测试
  - 有 README
  ```

### 💻 实现（120min）

- [ ] **[120min]** 在 `sandbox/tiny-projects/03-file-manager/` 下：

  ```
  03-file-manager/
  ├── .env.example
  ├── settings.py         # pydantic 配置
  ├── cli.py              # argparse 主入口
  ├── commands/
  │   ├── __init__.py
  │   ├── search.py       # 文件搜索
  │   ├── size.py         # 目录大小
  │   ├── duplicates.py   # 重复文件
  │   └── report.py       # 导出报告
  ├── tests/
  │   ├── test_search.py
  │   ├── test_size.py
  │   └── test_duplicates.py
  ├── README.md
  └── requirements.txt
  ```

  **1. `settings.py`**

  ```python
  from pathlib import Path
  from pydantic import BaseModel
  from dotenv import load_dotenv
  import os
  
  load_dotenv()
  
  class Settings(BaseModel):
      scan_root: Path = Path(os.getenv("SCAN_ROOT", "./"))
      max_depth: int = 5
      min_file_size: int = 0
  
  settings = Settings()
  ```

  **2. `commands/search.py`**

  ```python
  from pathlib import Path
  import fnmatch
  
  def search(pattern: str, root: Path, recursive: bool = True) -> list[Path]:
      """搜索匹配的文件
      
      Args:
          pattern: glob 模式，如
          root: 起始目录
          recursive: 是否递归
      """
      results = []
      if recursive:
          results = list(root.rglob(pattern))
      else:
          results = list(root.glob(pattern))
      return sorted(results)
  ```

  **3. `commands/size.py`**

  ```python
  from pathlib import Path
  
  def dir_size(path: Path) -> dict:
      """计算目录大小"""
      total = 0
      file_count = 0
      for f in path.rglob("*"):
          if f.is_file():
              total += f.stat().st_size
              file_count += 1
      return {
          "total_bytes": total,
          "total_mb": round(total / 1024 / 1024, 2),
          "file_count": file_count,
      }
  ```

  **4. `commands/duplicates.py`**

  ```python
  from pathlib import Path
  from collections import defaultdict
  
  def find_duplicates(root: Path) -> dict[list[Path]]:
      """找重复文件（基于 hash）"""
      hash_to_files = defaultdict(list)
      for f in root.rglob("*"):
          if f.is_file():
              file_hash = hash(f.read_bytes())
              hash_to_files[file_hash].append(f)
      
      return {
          h: files for h, files in hash_to_files.items()
          if len(files) > 1
      }
  ```

  **5. `cli.py`（主入口）**

  ```python
  import argparse
  from commands.search import search
  from commands.size import dir_size
  from commands.duplicates import find_duplicates
  from settings import settings
  import json
  
  def main():
      parser = argparse.ArgumentParser(prog="fmanager", description="文件管理 CLI")
      subparsers = parser.add_subparsers(dest="command", required=True)
      
      # search
      p_search = subparsers.add_parser("search", help="搜索文件")
      p_search.add_argument("pattern", help="glob 模式，如 *.py")
      p_search.add_argument("--no-recursive", action="store_true")
      
      # size
      p_size = subparsers.add_parser("size", help="目录大小")
      p_size.add_argument("path", nargs="?", default=".")
      
      # duplicates
      p_dup = subparsers.add_parser("dup", help="查找重复文件")
      p_dup.add_argument("path", nargs="?", default=".")
      
      args = parser.parse_args()
      
      if args.command == "search":
          results = search(args.pattern, settings.scan_root, not args.no_recursive)
          for f in results:
              print(f)
      elif args.command == "size":
          info = dir_size(Path(args.path))
          print(json.dumps(info, indent=2))
      elif args.command == "dup":
          dups = find_duplicates(Path(args.path))
          print(f"找到 {len(dups)} 组重复文件")
          for h, files in dups.items():
              print(f"\n组:")
              for f in files:
                  print(f"  {f}")
  
  if __name__ == "__main__":
      main()
  ```

### 💻 测试（45min）

- [ ] **[45min]** 写 5 条 pytest：

  ```python
  # tests/test_search.py
  from pathlib import Path
  from commands.search import search
  
  def test_search_finds_files(tmp_path):
      (tmp_path / "test.py").write_text("print('hi')")
      (tmp_path / "test.txt").write_text("hello")
      
      results = search("*.py", tmp_path)
      assert len(results) == 1
      assert results[0].name == "test.py"
  
  def test_search_recursive(tmp_path):
      (tmp_path / "sub").mkdir()
      (tmp_path / "sub" / "deep.py").write_text("# deep")
      
      results = search("*.py", tmp_path)
      assert len(results) == 1
      assert "deep.py" in str(results[0])
  
  # tests/test_size.py
  from commands.size import dir_size
  
  def test_dir_size(tmp_path):
      (tmp_path / "a.txt").write_text("x" * 100)
      (tmp_path / "b.txt").write_text("y" * 200)
      
      info = dir_size(tmp_path)
      assert info["file_count"] == 2
      assert info["total_bytes"] == 300
  
  # tests/test_duplicates.py
  from commands.duplicates import find_duplicates
  
  def test_find_duplicates(tmp_path):
      (tmp_path / "a.txt").write_text("same content")
      (tmp_path / "b.txt").write_text("same content")
      (tmp_path / "c.txt").write_text("different")
      
      dups = find_duplicates(tmp_path)
      assert len(dups) == 1
  ```

### 📝 README + 提交（25min）

- [ ] **[15min]** 写 README：

  ```markdown
  # File Manager CLI
  
  ## 安装
  pip pip install -r requirements.txt
  
  ## 使用
  ```bash
  python cli.py search "*.py"          # 搜索 .py 文件
  python cli.py size ./projects          # 目录大小
  python cli.py dup ./data               # 重复文件
  ```
  
  ## 测试
  ```bash
  pytest tests/
  ```
  ```

- [ ] **[10min]** Git commit：
  ```bash
  git add .
  git commit -m "feat(sandbox): file manager CLI with argparse + pydantic"
  ```

---

## 📚 Python 工程能力清单

完成这个项目后，你掌握了：
- [x] argparse 多子命令
- [x] pathlib 路径处理
- [x] pydantic 配置管理
- [x] python-dotenv 环境变量
- [x] pytest 测试
- [x] 模块化项目结构
- [x] Git 版本管理

---

## 📊 进度

```
W4 D5:    [░░░░░░░░░░] 0/1
W4 整体:  [░░░░░░░░░░] 0/13
阶段 1:   [░░░░░░░░░░] 0/46 (W2-4)
```

---

## ✅ 当日验收

- [ ] CLI 工具能跑（至少 3 个子命令）
- [ ] ≥ 5 条 pytest 测试通过
- [ ] README 写完
- [ ] Git commit

---

## 🎉 阶段 1 毕业 = Python 真正扎实

完成 W2-4 后，你的 Python 能力：
- ✅ 基础语法 + 函数 + 类
- ✅ 装饰器、生成器、async
- ✅ pydantic、dotenv、argparse
- ✅ LeetCode Easy 20 题
- ✅ Pythonic 风格
- ✅ 读过 LangChain 源码
- ✅ 完成 2 个综合项目

**这种 Python 基础做 Agent 开发绰绰有余**。

---

## 💡 周末预告

**W4 周日**：打开 [`W4-review.md`](W4-review.md) 做**阶段 1 毕业验收**