from line.simple_line_sentinel import SimpleLine

def check_loop_str(s):
    """使用链表判断回文字符串"""

    # 创建链表
    sl = SimpleLine()
    for c in s:
        sl.append(c)

    # 使用快慢指针找到中间结点
    p1 = sl.get_head()  # 慢结点
    p2 = sl.get_head()   # 快结点

    # 构建一个逆向链表
    sl2 = SimpleLine()
    while (p2 is not None) and (p2.next is not None):
        sl2.insert(0, p1.elem)
        p1 = p1.next
        p2 = p2.next.next

    if p2 and p2.next is None: # 是奇数个
        sl2.insert(0, p1.elem)
    
    sl2_p = sl2.get_head()
    while p1 is not None:
        if p1.elem != sl2_p.elem:
            return False
        p1 = p1.next
        sl2_p = sl2_p.next
    return True


if __name__ == '__main__':

    str1 = '1234321'
    str2 = '12344321'
    str3 = '12344320'

    print(check_loop_str(str1))
    print('='*10)
    print(check_loop_str(str2))
    print('='*10)
    print(check_loop_str(str3))

