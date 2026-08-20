# W15 D3 周三 · 2h — LeetCode 算法题

- **阶段**：7 求职冲刺 | **周次**：W15 | **状态**：⬜
- **主题**：Hot 100 算法题

---

## 🎯 今日目标（2 项）

- [ ] 至少 5 题能用最优解讲清
- [ ] 重点：数组 / 字符串 / 哈希 / 链表

---

## ✅ 任务清单（2h）

### 📚 数组 + 字符串 + 哈希（60min）

- [ ] **[60min]** 做 5 题（[LeetCode Hot 100](https://leetcode.cn/studyplan/top-100-liked/)）：
  - 两数之和（Hot 1）
  - 最长回文子串（Hot 5）
  - 无重复字符的最长子串（Hot 3）
  - 字母异位词分组（Hot 49）
  - 最长公共子序列（Hot 114）

### 📚 链表 + 二叉树（60min）

- [ ] **[60min]** 做 5 题：
  - 反转链表（Hot 206）
  - 合并两个有序链表（Hot 21）
  - 二叉树的最大深度（Hot 104）
  - 二叉树的层序遍历（Hot 102）
  - 验证二叉搜索树（Hot 98）

---

## 📚 答题模板

```python
# 1. 思路
"我的思路：... 时间复杂度 O(n)，空间 O(n)"

# 2. 代码
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

---

## ✅ 当日验收

- [ ] 至少 5 题用最优解讲清
- [ ] 能说出每题的时间空间复杂度

---

## 💡 明日预告

**W15 D4 周四**：模拟面试 1