def get_postorder(preorder, inorder):
    if not preorder:
        return ""
    root = preorder[0]
    idx = inorder.index(root)
    left_in = inorder[:idx]
    right_in = inorder[idx+1:]
    left_pre = preorder[1:1+len(left_in)]
    right_pre = preorder[1+len(left_in):]
    return get_postorder(left_pre, left_in) + get_postorder(right_pre, right_in) + root

try:
    while True:
        pre, ino = input().split()
        post = get_postorder(pre, ino)
        print(post)

except EOFError:
    pass