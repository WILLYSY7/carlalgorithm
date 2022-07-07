'''

涉及到的题目
leetcode 735 （同剑指offer II 037）

'''
'''
剑指 Offer II 037. 小行星碰撞
给定一个整数数组 asteroids，表示在同一行的小行星。
对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。
找出碰撞后剩下的所有小行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

示例 1：
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。

示例 2：
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。

示例 3：
输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

示例 4：
输入：asteroids = [-2,-1,1,2]
输出：[-2,-1,1,2]
解释：-2 和 -1 向左移动，而 1 和 2 向右移动。 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。 
'''
'''
当栈顶为空，或者行星为正数的时候就统统入栈，说明此时行星全部向右移动，且不会互相碰撞
    比如，栈里已经存在了向左运行的行星（即负数），这个时候正数入栈，行星右移动，肯定不会相撞，因为已经分头错开了
当遍历到负数的时候，说明行星开始向左运动了，开始判断栈顶的元素和该行星是否会相撞
    循环判断：
    1.栈顶为正数，那么一定相撞，保留绝对值较大的数
    2.栈顶为负数，那么直接入栈，不会相撞，全都向左移动
    3.栈顶为正数，且和行星数值一样，直接弹出栈顶，然后退出循环
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            if not res or i > 0 or i * res[-1] > 0: res.append(i)
            if i < 0 and res[-1] > 0:
                while True:
                    if abs(i) == res[-1] > 0:
                        res.pop()
                        break
                    elif abs(i) > res[-1] > 0:
                        res.pop()
                        if not res:
                            res.append(i)
                            break
                    elif abs(i) < res[-1] and res[-1] > 0:
                        break
                    else:
                        res.append(i)
                        break
        return res