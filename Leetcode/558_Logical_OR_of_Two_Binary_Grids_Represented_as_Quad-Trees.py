class Solution:
    def intersect(self, quadTree1, quadTree2):
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2

        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        top_left = self.intersect(
            quadTree1.topLeft, quadTree2.topLeft
        )
        top_right = self.intersect(
            quadTree1.topRight, quadTree2.topRight
        )
        bottom_left = self.intersect(
            quadTree1.bottomLeft, quadTree2.bottomLeft
        )
        bottom_right = self.intersect(
            quadTree1.bottomRight, quadTree2.bottomRight
        )

        children = [top_left, top_right, bottom_left, bottom_right]

        if all(child.isLeaf for child in children):
            value = children[0].val
            if all(child.val == value for child in children):
                return Node(value, True, None, None, None, None)

        return Node(
            True,
            False,
            top_left,
            top_right,
            bottom_left,
            bottom_right
        )
