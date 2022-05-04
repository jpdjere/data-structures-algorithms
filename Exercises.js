// #> Arrays: Two Sum

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {};
    for (let i = 0; i < nums.length; i++) {
        let current = nums[i];
        let complement = current - target
        if(seen[complement]) {
            return [seen[complement], i]
        }
        seen[current] = i
    }
    return false;
    
};

//#> Arrays: Best Time to Buy and Sell Stock (Easy)

/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    let maxProfit = 0;
    let minPrice = Number.POSITIVE_INFINITY;
    for(let price of prices) {
        maxProfit = Math.max(maxProfit, price - minPrice)
        if(price < minPrice) {
            minPrice = price;
        }
    }
    return maxProfit
};

// #> Contains Duplicate

var containsDuplicate = function(nums) {
  const seen = {};
  for(let num of nums) {
      if(seen[num] !== undefined) {
          return true;
      }
      seen[num] = true;
  }  
  return false;
};

// #> Product of Array Except Self

// Approach 1
var productExceptSelf = function(nums) {
    let product = 1;
    let zeroes = 0;
    for(let num of nums) {
        if(num) {
            product = product * num;
        } else {
            zeroes++;
        }
    }
    const answer = nums.map(num => {
        if(zeroes > 1) {
            return 0
        }
        if(zeroes === 1) {
            if(num === 0) {
                return product
            }
            return 0
        }
        return product * Math.pow(num, -1)
    })
    return answer;
};

// Approach 2
var productExceptSelf = function(nums) {
    let leftProduct = 1;
    let leftArray = [1];
    for (let i = 1; i < nums.length; i++) {
        leftProduct = leftProduct * nums[i - 1];
        leftArray.push(leftProduct);
    }

    let rightProduct = 1;
    let rightArray = [1];
    for (let j = nums.length - 2; j > -1; j--) {
        rightProduct = rightProduct * nums[j + 1];
        rightArray.push(rightProduct);
    }
    rightArray = rightArray.reverse();

    const ans = [];
    for (let k = 0; k < nums.length; k++) {
        ans.push(leftArray[k] * rightArray[k])
    }
    return ans;
}

// #> Maximum Subarray

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxEndingHere = nums[0];
    let maxSoFar = nums[0];
    for (let num of nums.slice(1)) {
        maxEndingHere = Math.max(num, maxEndingHere + num);
        maxSoFar = Math.max(maxEndingHere, maxSoFar)
    }
    return maxSoFar;
};

// #> Container with the Most Water
// area = (b - a) * min(heights[a], heights[b])

var maxArea = function(height) {
    let maxWater = 0;
    let a = 0;
    let b = height.length - 1;
    while(a !== b) {
        if(height[a] < height[b]) {
            let water = (b - a) * height[a];
            maxWater = Math.max(maxWater, water)
            a++;
        } else {
            let water = (b - a) * height[b];
            maxWater = Math.max(maxWater, water);
            b--;
        }
    }
    return maxWater;
};

// #> Trapping Rainwater
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let a = 0;
    let b = height.length - 1;
    let maxLeft = 0;
    let maxRight = 0;
    let trappedWater = 0;
    while(a !== b) {
        if(height[a] < height[b]) {
            if(maxLeft > height[a]) {
                const waterToSum = maxLeft - height[a] > 0 ? maxLeft - height[a] : 0
                trappedWater = trappedWater + waterToSum;
            } else {
                maxLeft = height[a]
            }
            a++;
        } else {
            if(maxRight > height[b]) {
                const waterToSum = maxRight - height[b] > 0 ? maxRight - height[b] : 0
                trappedWater = trappedWater + waterToSum;
            } else {
                maxRight = height[b];
            }
            b--;
        }
    }
    return trappedWater;
};

// #> Best Time to Buy and Sell Stock II

var maxProfit = function(prices) {
    let minPrice = Number.MAX_SAFE_INTEGER;
    let maxProfit = 0;
    for(let price of prices) {
        currentLocalProfit = maxProfit + price - minPrice;
        if(currentLocalProfit > maxProfit) {
            maxProfit = currentLocalProfit;
            minPrice = Number.MAX_SAFE_INTEGER;
        }
        if(price < minPrice) {
            minPrice = price
        }
    }
    return maxProfit;
};

// #> Maximum Product Subarray
var maxProduct = function(nums) {
    let maxProduct = nums[0];
    let minProduct = nums[0];
    let maxTotal = nums[0]
    for(let num of nums.slice(1)) {
        let savedMinProduct = minProduct;
        minProduct = Math.min(num, maxProduct * num, savedMinProduct * num);
        maxProduct = Math.max(num, maxProduct * num, savedMinProduct * num);
        maxTotal = Math.max(maxProduct, maxTotal)
    }
    return maxTotal
};

// #> 3 Sum

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var threeSum = function(nums) {
    let result = new Set();

    // 1. Split into list of negative, positive and zeroes
    const zeroes = [];
    const positives = [];
    const negatives = [];
    for(let num of nums) {
        if(num < 0) {
            negatives.push(num);
        } else if (num > 0) {
            positives.push(num);
        } else {
            zeroes.push(num);
        }
    }

    // 2. Create set for positive and negatives for O(1) lookup
    let N = new Set(negatives);
    let P = new Set(positives);

    // 3. If there is at least 1 zero in the least, add all cases where (-x, 0, x)
    if(zeroes.length) {
        for(let positive of positives) {
            if (N.has(-1 * positive)) {
                result.add([-1 * positive, 0, positive])
            }
        }
    }

    // 4. If there is 3 zeroes in the list, include that case also:
    if(zeroes.length >= 3) {
        result.add([0, 0, 0]);
    }

    // 5. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    // existis in the positive number set:
    for(let i = 0; i < negatives.length; i++) {
        for(let j = i + 1; j < negatives.length; j++) {
            let complement = 0 - negatives[i] - negatives[j];
            if(P.has(complement)) {
                result.add([negatives[i], complement, negatives[j]].sort());
            }
        }
    }

    // 6. And the same but opposite: for all pairs of positive numbers (3, 1), check to see if
    // their complement (-4) exists in the negative number set:
    for(let i = 0; i < positives.length; i++) {
        for(let j = i + 1; j < positives.length; j++) {
            let complement = 0 - positives[i] - positives[j];
            if(N.has(complement)) {
                result.add([positives[i], complement, positives[j]].sort())
            }
        }
    }

    return [...new Set([...result].map(arr => JSON.stringify(arr)))].map(arr => JSON.parse(arr));

}


// #> Arrays: Search in Rotated Sorted Array

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
    if(nums.length === 0) {
        return -1
    }

    let left = 0;
    let right = nums.length - 1;
    while(left <= right) {
        let mid = Math.floor((right + left) / 2);

        if(nums[mid] === target){
            return mid;
        }

        // Where is our inflection point?

        // Is it to my right?
        if(nums[mid] >= nums[left]) {
            // Then our inflection point is to the right of mid, the left side is normally increasing.
            // Now we try to see if our target is in the left side:
            if(nums[left] <= target && target <= nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // Our inflection point is to the left of mid, the right side is normally increasing
            if(nums[mid] <= target && target <= nums[right]) {
                left = mid + 1
            } else {
                right = mid - 1;
            }
        }

    }
    return -1;
};

// #> Strings: Valid Palindrome

var isPalindrome = function(s) {
    const lowercase_s = s.toLowerCase();
    const alphanum = lowercase_s.split("").map(char => {
        if(char.match(/^[0-9a-z]+$/)) {
            return char;
        }
        return ""
    });
    
    return alphanum.join("") === alphanum.reverse().join("")
};

// #> Valid Parentheses

var isValid = function(s) {
    const pairs = {
        "}":"{",
        "]":"[",
        ")":"("
    };
    const open = new Set(["{", "[", "("]);
    const stack = [];
    for(let c of s) {
        if(open.has(c)) {
            stack.push(c);
            continue;
        }
        if(stack.length === 0) {
            return false;
        }
        if(stack[stack.length - 1] !== pairs[c]) {
            return false
        }
        stack.pop();
    }
    return stack.length === 0;
};


// #> Minimum Remove to Make Valid Parentheses

/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    const openIdx = [];
    const invalid = [];
    for(let i = 0; i < s.length; i++) {
        const char = s[i];
        if(char === "(") {
            openIdx.push(i);
        } else if(char === ")") {
            if(openIdx.length === 0) {
                invalid.push(i);
            } else {
                openIdx.pop();
            }
        }
    }
    const allInvalid = invalid.concat(openIdx);
    return s.split("").filter((char, idx) => !allInvalid.includes(idx)).join("");
};

// #> Strings: Longest Palindromic Substring

var longestPalindrome = function(s) {
    let longestSubstring = "";
    for(let i = 0; i < s.length; i++) {
        let oddCandidate = isPalindrome(s, i, i);
        if(oddCandidate.length > longestSubstring.length) {
            longestSubstring = oddCandidate;
        }

        let evenCandidate = isPalindrome(s, i, i+1);
        if(evenCandidate.length > longestSubstring.length) {
            longestSubstring = evenCandidate;
        }
    }
    return longestSubstring;
};

var isPalindrome = function(str, i, j) {
    while(i >= 0 && j < str.length && str[i] === str[j]) {
        i--;
        j++
    }
    // Because I have moved one extra to the sides, and only then realized
    // that my current pair doesn't match, I need to adjust the indeces.
    // i moves one position inwards, and j is not included so the current j is OK
    return str.slice(i+1, j)
}

// #> Strings: Valid Anagram

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    const seen = {};
    for(let char of s) {
        if(seen[char]) {
            seen[char]++;
        } else {
            seen[char] = 1;
        }
    }
    for(let char of t) {
        if(seen[char] && seen[char] > 0) {
            seen[char]--;
        } else {
            return false;
        }
    }
    const pending = Object.keys(seen).map(key => seen[key]).reduce((acc, curr) => acc+curr, 0);
    
    return pending <= 0;
};

// #> Strings: Palindromic Substrings

var countSubstrings = function(s) {
    let totalCount = 0;
    for(let i = 0; i < s.length; i++) {
        totalCount += isPalindrome(s, i, i);
        totalCount += isPalindrome(s, i, i + 1);
    }
    return totalCount
    
};

var isPalindrome = function(str, i, j) {
    let count = 0;
    while(i >= 0 && j < str.length && str[i] === str[j]) {
        count += 1;
        i--;
        j++;
    }
    return count;
}

// #> Trees: Maximum Depth of Binary Tree

var maxDepth = function(root) {
    return recursiveDFS(root)
};

var recursiveDFS = function(node, depth = 0) {
    if(!node) {
        return depth;
    }
    return Math.max(recursiveDFS(node.left, depth + 1), recursiveDFS(node.right, depth + 1))
}

// #> Trees: Same Tree
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
 var isSameTree = function(p, q) {
    return recursiveSameTree(p, q)
};

var recursiveSameTree = function(nodeA, nodeB) {
    // Base case: reached end of branch
    if(!nodeA && !nodeB) {
        return true
    }
    // Base case: one node exists and the other one doesn't
    if(nodeA && !nodeB) {
        return false;
    }
    if(!nodeA && nodeB) {
        return false
    }
    // If both exists AND are equal, check their children recursively
    if(nodeA.val === nodeB.val) {
        return recursiveSameTree(nodeA.left, nodeB.left) && recursiveSameTree(nodeA.right, nodeB.right);
    } else {
    // Otherwise, they are different trees
        return false
    }
}

// #> Trees: Invert/Flip Binary Tree

var invertTree = function(root) {
    if(!root) {
        return null;
    }
    recursiveRevert(root)
    return root;
};

var recursiveRevert = function(node) {
    if(!node) {
        return;
    }

    [node.left, node.right] = [node.right, node.left]
    recursiveRevert(node.left);
    recursiveRevert(node.right);
}


// #> Trees: Binary Tree Level Order Traversal

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
 var levelOrder = function(root) {
    if(!root) {
        return [];
    }
    const answer = [];
    const q = [root];
    let counter = q.length;
    let currentLevel = []

    while(q.length > 0) {
        counter--;
        const current = q.shift();
        currentLevel.push(current.val);
        
        current.left && q.push(current.left);
        current.right && q.push(current.right);
        
        if(counter === 0) {
            answer.push(currentLevel);
            currentLevel = [];
            counter = q.length;
        }
    }
    return answer;
};

// #> Trees: Binary Tree Right Side View 

var rightSideView = function(root) {
    if(!root) {
        return [];
    }
    const ans = [];
    q = [root];
    let counter = q.length;
    
    while(q.length > 0) {
        counter--;
        const current = q.shift();
        current.left && q.push(current.left);
        current.right && q.push(current.right);
        
        if(counter === 0) {
            ans.push(current.val);
            counter = q.length;
        }
    }
    
    return ans;
};

// #> Average of Levels in Binary Tree

var averageOfLevels = function(root) {
    const ans = [];
    q = [root];
    let counter = q.length;
    let levelCounter = q.length;
    let levelSum = 0

    while(q.length > 0) {
        counter--;
        const current = q.shift();
        levelSum += counter.val;
        current.left && q.push(current.left);
        current.right && q.push(current.right);

        if(counter == 0) {
            ans.push(levelSum / levelCounter);
            counter = q.length;
            levelCounter = counter;
            levelSum = 0;
        }
    }
    return ans;
};


// #> Trees: Subtree of Another Tree (Easy)
var isSubtree = function(root, subRoot) {
    if(!root) {
        return false;
    }
    if(isMatch(root, subRoot)) {
        return true
    }
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

var isMatch = function(node, subRoot) {
    if((!node && subRoot) || (node && !subRoot)) {
        return false
    }
    if(!node && !subRoot) {
        return true
    }
    if(node.val === subRoot.val) {
        return isMatch(node.left, subRoot.left) && isMatch(node.right, subRoot.right);
    } else {
        return false;
    }
}


// #> Validate Binary Search Tree (Medium)

var isValidBST = function(root) {
    return recursiveCheck(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)    
};

var recursiveCheck = function(node, minVal, maxVal) {
    if(!node) {
        return true;
    }
    if(node.val >= maxVal || node.val <= minVal) {
        return false
    }
    return recursiveCheck(node.left, minVal, node.val) && recursiveCheck(node.right, node.val, maxVal)
}


    //         -inf inf
    //             5
    // -inf  5            5   inf        
    //     1                7
    //               5   7       7  inf
    //                 6          8


// #> Trees: Lowest Common Ancestor of a BST (Easy)
var lowestCommonAncestor = function(root, p, q) {
    return recursive(node, p, q)
};

var recursive = function(node, p, q) {
    if((p.val <= node.val && node.val <= q.val) || (q.val <= node.val && node.val <= p.val)) {
        return node
    }
    if(p.val < node.val) {
        return recursive(node.left, p, q);
    }
    return recursive(node.right, p, q)
}

// #> Trees: Lowest Common Ancestor of a Binary Tree (Medium)
var lowestCommonAncestor = function(root, p, q) {
    return recursiveLCA(root, p, q)
};

var recursiveLCA = function(node, p, q) {
    if(!node) {
        return null;
    }
    if(node === p || node === q) {
        return node;
    }

    let left = recursiveLCA(node.left, p, q);
    let right = recursiveLCA(node.right, p, q);

    if(left && right) {
        return node;
    }

    return left || right;
}

// #> Trees: Kth Smallest Element in a BST (Medium)

// Approach 1: Using DFS to create inorder (ordered list) and then return K - 1
var kthSmallest = function(root, k) {
    const inorder = [];
    dfs(root, inorder)
    return inorder[k - 1]
};

var dfs = function(node, inorder) {
    if(node.left) {
        dfs(node.left, inorder)
    }
    inorder.push(node.val);
    if(node.right) {
        dfs(node.right, inorder)
    }

}

// Approach 2: Iterative Inorder Traversal, with the help of a stack
// See explantion in Python version.
var kthSmallest = function(root, k) {
    const stack = [];
    let node = root;

    while(true) {
        while(node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop();
        k--;
        if(k === 0) {
            return node.val
        }
        node = node.right;
    }
};

// #> Trees: Construct Binary Tree from Preorder and Inorder Traversal (Medium)
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
//  preorder = [3,9,20,15,7]
//  inorder = [9,3,15,20,7]
var buildTree = function(preorder, inorder) {
    if(inorder.length === 0) {
        return null;
    }
    
    const root = preorder.shift(); // Por alguna razon esto tiene que estar en una linea aparte
    let indexOfRootInInorder = inorder.findIndex(val => val === root);
    let node = new TreeNode(inorder[indexOfRootInInorder]);

    node.left = buildTree(preorder, inorder.slice(0, indexOfRootInInorder))
    node.right = buildTree(preorder, inorder.slice(indexOfRootInInorder + 1))

    return node
};








// #> Linked Lists: Reverse a Singly Linked List
var reverseList = function(head) {
    if(!head || !head.next) {
        return head;
    }
    let first = head;
    let second = first.next;
    
    first.next = null;
    
    while(second) {
        let secondNext = second.next;
        
        second.next = first
        
        first = second
        second = secondNext
    }
    
    return first
    
    
};


// #> Linked Lists: M, N reversals - Reverse Linked Lists between M and N

//      pl   l         r   pr
// 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

// 1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7

// pl -> r
// l -> pr
var reverseBetween = function(head, left, right) {
    let currentPosition = 1;
    let preLeft = head;
    let leftLimit = head;

    while(currentPosition < left) {
        preLeft = leftLimit;
        leftLimit = leftLimit.next;

        currentPosition++;
    }

    let pl = preLeft;
    let l = leftLimit;

    let first = leftLimit;
    let second = first.next;

    while(currentPosition < right) {
        let secondNext = second.next;

        second.next = first;

        first = second;
        second = secondNext;

        currentPosition++;
    }

    let r = first;
    let pr = second;

    pl.next = r;
    l.next = pr;

    if(left === 1) {
        return right;
    }
    return head;
}

// #> Linked Lists: Cycle Detection

var hasCycle = function(head) {
    if(!head) {
        return false;
    }
    let turtle = head;
    let hare = head;
    
    while(true) {
        turtle = turtle.next;

        if(!hare.next || !hare.next.next) {
            return false
        }

        hare = hare.next.next;

        if(turtle === hare) {
            return true
        }

    }
};

// #> Linked Lists: Linked List Cycle II

var detectCycle = function(head) {
    if(!head || !head.next) {
        return null;
    }
    let turtle = head;
    let hare = head;

    while(true) {
        turtle = turtle.next;

        if(!hare.next || !hare.next.next) {
            return null;
        }

        hare = hare.next.next;

        if(turtle === hare) {
            break;
        }
    }

    let p1 = turtle;
    let p2 = head;

    while(p1 !== p2) {
        p1 = p1.next;
        p2 = p2.next;
    }
    return p1;
};

// # Linked Lists: Flatten a Multi-Level Doubly-Linked List (Medium)

var flatten = function(head) {
    let current = head;
    while(current) {
        let currNext;
        if(current.child) {
            currNext = current.next;
            current.next = current.child;
            current.next.prev = current;
            current.child = null;
            
            let currentOfNewLayer = current.next;
            while(currentOfNewLayer.next) {
                currentOfNewLayer = currentOfNewLayer.next;
            }
            let lastOfNewLayer = currentOfNewLayer;
            if(currNext) {
                currNext.prev = lastOfNewLayer;
                lastOfNewLayer.next = currNext;
            }

        }
        
        current = current.next;
    }
    return head;
};


// # Linked Lists: Remove Nth Node From End of List
var removeNthFromEnd = function(head, n) {
    if(!head.next) {
        return null;
    }
    let nodes = 0;
    let current = head;
    while(current) {
        nodes++;
        current = current.next;
    }
    let target = nodes - n; // 2 - 2 = 0
    
    // Special case in which the node to remove is the first one
    if(target === 0) {
        head = head.next;
        return head;
    }

    let counter = 1;
    let currentNode = head;
    while(counter < target) { // 1 < 0
        counter++;
        currentNode = currentNode.next;
    }
    currentNode.next = currentNode.next.next;
    
    return head;
    
};

// # Linked Lists: Reorder List (Medium)
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
 var reorderList = function(head) {
    if(!head.next || !head.next.next) {
        return head;
    };
    
    let current = head;
    let stack = [];
    while(current) {
        stack.push(current)
        current = current.next;
    }

    let numberOfNodes = stack.length;
    let tailNumber = Math.ceil(numberOfNodes / 2);

    let counter = 1;
    let newCurrent = head;
    while(counter <= tailNumber){
        let nodeToInsert = stack.pop();
        let nextNewCurrent = newCurrent.next;
        newCurrent.next = nodeToInsert;
        nodeToInsert.next = nextNewCurrent;
        newCurrent = newCurrent.next.next;
        counter++;
    }
    newCurrent.next = null;
    
};


// #> Linked Lists: Merge Two Sorted Lists
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
 var mergeTwoLists = function(list1, list2) {
    const dummy = new ListNode(0, null);
    let currentNode = dummy;
    
    while(list1 && list2) {
        if(list1.val <= list2.val) {
            currentNode.next = list1;
            list1 = list1.next;
        } else {
            currentNode.next = list2;
            list2 = list2.next
        }
        currentNode = currentNode.next;
    }
    
    if(list2) {
        currentNode.next = list2
    } else {
        currentNode.next = list1
    }
    
    return dummy.next;
};


// #> Graphs: Time Needed to Inform All Employees (Medium)

var numOfMinutes = function(n, headID, manager, informTime) {
    const adjList = createAdjacencyList(manager);
    return recursive(headID, adjList, informTime)
};

var recursive = function(employeeId, adjList, informTime) {
    const managed = adjList[employeeId];
    if(managed.length === 0) {
        return informTime[employeeId];
    } 
    return informTime[employeeId] + Math.max(...managed.map((managedId) => {
        return recursive(managedId, adjList, informTime)
    }));
}

var createAdjacencyList = function(managerArray) {
    const adjList = new Array(managerArray.length).fill(0).map(employee => []);
    for(let employeeId = 0; employeeId < managerArray.length; employeeId++) {
        let manager = managerArray[employeeId];
        if(manager === -1 ) {
            continue
        }
        adjList[manager].push(employeeId)
    }
    return adjList;
}


// #> Graphs: Number of Islands (Medium)

var numIslands = function(grid) {
    let rows = grid.length;
    let columns = grid[0].length;
    
    let counter = 0;
    
    let visited = new Array(rows).fill(0).map(row => new Array(columns).fill(""));
    
    for(let i = 0; i < rows; i++) {
        for(let j = 0; j < columns; j++) {
            if(grid[i][j] === "1" && visited[i][j] !== "V") {
                counter++;
                recursive(i, j, rows, columns, grid, visited)
            }
        }
    }
    return counter;
}

var recursive= function(i, j, rows, columns, grid, visited) {
    if(i < 0 || i >= rows || j < 0 || j >= columns) {
        return
    }
    
    if(grid[i][j] === "0" || visited[i][j] === "V") {
        return
    }
    
    visited[i][j] = "V";
    recursive(i + 1, j, rows, columns, grid, visited);
    recursive(i - 1, j, rows, columns, grid, visited);
    recursive(i, j + 1, rows, columns, grid, visited);
    recursive(i, j - 1, rows, columns, grid, visited);
}

// #> Graphs: Recursive BFS

var traversalBFS = function(graph) {
    const res = [];
    const seen = {};
    const q = [0];

    while(q.length > 0) {
        const current = q.shift();
        res.push(current);
        seen[current] = true;
        const neighbours = graph[current];
        
        for(let neighbour of neighbours) {
            if(!seen[neighbour]) {
                q.push(neighbour);
            }
        }
    }
    return res;
}

// #> Graphs: Recursive DFS

var traversalDFS = function(graph) {
    const res = [];
    const seen = {};
    recursiveDFS(0, res, seen);
    return res;
}

var recursiveDFS = function(node, res, seen, graph) {
    res.append(node);
    seen[node] = true;
    let neighbours = graph[node];
    for(let neighbour of neighbours) {
        if(!seen[neighbour]) {
            recursiveDFS(neighbour, res, seen, graph)
        }
    }

}



// #> Graphs: Clone Graph 

var cloneGraph = function(node) {
    if(!node) {
        return null;
    }
    const graphMap = {}
    const q = [node]
    
    graphMap[node.val] = new Node(node.val);
    
    while(q.length > 0) {
        const current = q.shift()
        const neighbors = current.neighbors;
        for (let neighbor of neighbors) {
            if(!graphMap[neighbor.val]) {
                graphMap[neighbor.val] = new Node(neighbor.val);
                q.push(neighbor)
            }
            graphMap[current.val].neighbors.push(graphMap[neighbor.val])
        }
    }
    
    return graphMap[node.val]
}


// #> Graphs: Course Scheduler (Medium)
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
 var canFinish = function(numCourses, prerequisites) {
    // Create and indegree array
    let indegree = createIndegree(numCourses, prerequisites);
    // Create an adjacency lost
    let adjList = createAdjList(numCourses, prerequisites);
    
    // Start topoligical sort
    // Create a stack to keep in it the index of the values with 0 indegree
    const stack = [];
    for (let i = 0; i < indegree.length; i++) {
        if(indegree[i] === 0) {
            stack.push(i)
        }
    }
    // Create a counter to keep track of how many node we have removed from indegree array
    let counter = 0
    
    // Actually do topological sort
    while(stack.length > 0) {
        counter++;
        
        const current = stack.pop();
        const neighbors = adjList[current];
        
        for(let neighbor of neighbors) {
            indegree[neighbor]--;
            if(indegree[neighbor] === 0) {
                stack.push(neighbor)
            }
        }
    }
    if(counter === numCourses) {
        return true
    }
    return false;
};

var createIndegree = function(numCourses, prerequisites) {
    const indegree = new Array(numCourses).fill(0);
    for(let [target, origin] of prerequisites) {
        indegree[target]++;
    }
    return indegree;
}

var createAdjList = function(numCourses, prerequisites) {
    const adjList = new Array(numCourses).fill(1).map(el => []);
    for(let [target, origin] of prerequisites) {
        adjList[origin].push(target);
    }
    return adjList;
}


// #> Graphs: Course Scheduler II (Medium)
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
 var findOrder = function(numCourses, prerequisites) {
    const indegree = createIndegree(numCourses, prerequisites);
    const adjList = createAdjList(numCourses, prerequisites);
    
    const stack = [];
    for(let i = 0; i < indegree.length; i++) {
        if(indegree[i] === 0) {
            stack.push(i)
        }
    }
    
    let counter = 0;
    const res = []
    
    while(stack.length > 0) {
        counter++;
        
        const current = stack.pop();
        res.push(current);
        const neighbors = adjList[current];
        
        for(let neighbor of neighbors) {
            indegree[neighbor]--;
            if(indegree[neighbor] === 0) {
                stack.push(neighbor);
            }
        }
    }
    if(counter === numCourses) {
        return res;
    }
    return [];
};

var createIndegree = function (numCourses, prerequisites) {
    const indegree = new Array(numCourses).fill(0);
    for(let [target, origin] of prerequisites) {
        indegree[target]++;
    }
    return indegree;
}

var createAdjList = function (numCourses, prerequisites) {
    const adjList = new Array(numCourses).fill(0).map(el => []);
    for(let [target, origin] of prerequisites) {
        adjList[origin].push(target)
    }
    return adjList;
}


// #> Intervals: Insert Interval (Medium)
/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */

// intervals = [[1,3],[6,9]], newInterval = [2,5]

var insert = function(intervals, newInterval) {
    const res = [];
    
    let idx = 0;
    for(let currentInterval of intervals) {
        let [currentStart, currentEnd] = currentInterval;
        let [newStart, newEnd] = newInterval;
        
        if(newEnd < currentStart) {
            res.push(newInterval);
            return res.concat(intervals.slice(idx))
        } else if(newStart > currentEnd) {
            res.push(currentInterval)
        } else {
            newInterval = [Math.min(newStart, currentStart), Math.max(newEnd, currentEnd)]
        }
        
        idx++;
    }
    
    res.push(newInterval);
    return res;
    
};


// #> Intervals: Merge Intervals (Medium)
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */

// [[1,3],[2,6],[8,10],[15,18]]
var merge = function(intervals) {
    const res = [];
    const sortedIntervals = intervals.sort((a,b) => a[0] - b[0]);
    
    for(let currentInterval of sortedIntervals) {
        let [currentStart, currentEnd] = currentInterval;

        const last = res[res.length - 1];
        if(res.length > 0 && currentStart <= last[1]) {
            res[res.length - 1] = [Math.min(currentStart, last[0]), Math.max(currentEnd, last[1])]
        } else {
            res.push(currentInterval)
        }
        
    }
    return res;
    
};







// #> Intervals: Non-overlapping Intervals (Medium)
/**
 * @param {number[][]} intervals
 * @return {number}
 */

// [[1,2], [1,3],[2,3],[3,4],]

// [[-1,1],[3,4],[10,11],[12,14]]
var eraseOverlapIntervals = function(intervals) {
    let res = [];
    let counter = 0;
    const sortedIntervals = intervals.sort((a,b) => a[0] - b[0]);

    for(let currentInterval of sortedIntervals) {
        let [currentStart, currentEnd] = currentInterval;

        const last = res[res.length - 1];
        if(res.length > 0 && currentStart < last[1]) {
            counter++;
            res[res.length - 1] = currentEnd > last[1] ? last : currentInterval;
        } else {
            res.push(currentInterval);
        }
    }
    return counter;
};