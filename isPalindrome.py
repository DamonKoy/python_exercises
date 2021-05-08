"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def isPalindrome(text: str):
    list = []
    for i in text:
        if i.isdigit() or i.isalpha():
            list.append(i)
    if ''.join(list).lower() == ''.join(list[::-1]).lower():
        return True
    else:
        return False


def isPalindrome2(text: str):
    """
    双指针验证回文
    :param text:
    :return:
    """
    # 定义前后两个指针
    left = 0
    right = len(text) - 1

    while(left <= right):
        # 判断左指针是否为字母或数字，否则往后移一位，直到是
        while not(text[left].isdigit() or text[left].isalpha()):
            left = left + 1

        # 判断右指针是否为字母或数字，否则往前移一位，直到是
        while not(text[right].isdigit() or text[right].isalpha()):
            right = right - 1

        # 判断小写字母或数字的值是否一致，否则返回False，是则继续移动指针
        if text[left].lower() != text[right].lower():
            return False
        else:
            left, right = left + 1, right - 1
    return True


print(isPalindrome2('A man, a plan, a canal: Panama'))

