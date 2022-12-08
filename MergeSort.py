# Merge Sort

def msort(nums: List[int]) -> None:
    def msort_helper(nums: List[int], l: int, r: int) -> None:
        if l >= r: return
        m = (l + r) // 2
        msort_helper(nums, l, m)
        msort_helper(nums, m + 1, r)
        merge(nums, l, r)
    def merge(nums: List[int], l: int, r: int) -> None:
        m = (l + r) // 2
        i, j = l, m + 1
        list = []
        for k in range(r - l + 1):
            if j > r or (i <= m and nums[i] < nums[j]): 
                list.append(nums[i])
                i += 1
            else: 
                list.append(nums[j])
                j += 1
        for k in range(len(list)):
            nums[l] = list[k]
            l += 1
    msort_helper(nums, 0, len(nums) - 1)
