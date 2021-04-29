""" partition最优方法为双指针j=hi+1, i = lo.   将左边大于pivot和右边小于pivot的互换位置
最后的终止条件为i>=j （相等的时候的情况为num[j]==pivot）

循环交换nums[i] 和 nums[j] 最后交换nums[j] 和pivot

跳出循环交换nums[j]和pivot。 因为while (nums[++i] < pivot) 和 while (nums[--j] > pivot)
j最后的位置一定为最后一个小于pivot的位置上。最终i肯定停在最开始的一个nums[i] > pivot	的位置上，肯定不能用大于pivot的数字和pivot交换，如果这样交换左边就有大于pivot的数字了
"""