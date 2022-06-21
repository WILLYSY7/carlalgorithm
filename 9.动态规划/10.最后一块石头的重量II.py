'''

涉及到的题目
leetcode 1049

'''
'''
leetcode 1049
1049. 最后一块石头的重量 II
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

示例 1：
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

示例 2：
输入：stones = [31,26,33,21,
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 尽可能将石头分成重量相同的两堆，这样两堆开始撞的时候剩余的石头是最少的
        # 难的就是如何想到这一步
        # 我们可以假设第一次选a，b两块石头对撞，剩余a-b (假设a>b)
        # 第二次选c，d两块石头对撞，剩余c-d(假设c>d)
        # 这样一直撞下去，剩余的就是 a-b+c-d+....=a+c-(b+d)-...===>我们需要这个值尽可能小
        # 所以最小就是0，最完美的情况就是a+c+.... == b+d+.... = sum/2
        # 所以我们就要求出两个子区间，（两堆质量尽可能相近的石头）使得两个子区间里元素和尽可能接近
        # 所以就直接对sum整除2，然后转换成背包问题即可
        total = sum(stones)
        target_value = total // 2
        dp = [0]*(target_value+1)
        for i in range(len(stones)):
            for j in range(target_value, stones[i]-1, -1):
                dp[j] = max(dp[j], stones[i] + dp[j-stones[i]])
        half = dp[-1]
        return abs(total - half*2)