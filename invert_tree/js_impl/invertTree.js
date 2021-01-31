class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(data) {
        const node = new Node(data);
        if (this.root === null) {
            this.root = node;

        } else {
            this.insertNode(this.root, node);
        }

    }

    insertNode(rootNode, newNode) {
        //move to left
        if (newNode.left < rootNode.root) {
            console.log(`lefy node is ${newNode.left}`)
            //if left is null
            if (rootNode.left === null) {
                rootNode.left = newNode;
            } else {
                this.insertNode(rootNode.left, newNode);
            }
        } else {
            console.log(`right node is ${newNode.right}`)
                if (rootNode.right === null) {
                    rootNode.right = newNode;
                } else {
                    this.insertNode(rootNode.right, newNode);
                }
            }
        }
}

const invertTree = (tree) => {
    if (!tree) {
        return;
    }
    const left = invertTree(tree.left);
    const right = invertTree(tree.right);
    tree.left = right;
    tree.right = left;
    return tree;
}


const binaryTree = new BinaryTree();
binaryTree.insert(8);
binaryTree.insert(3);
binaryTree.insert(10);
binaryTree.insert(14);
binaryTree.insert(6);
binaryTree.insert(1);
binaryTree.insert(4);
binaryTree.insert(7);
binaryTree.insert(13);

console.log(binaryTree)