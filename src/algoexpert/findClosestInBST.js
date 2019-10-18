// Average: O(logn) time | [recursive] O(logd) space (d = depth of BST) | [iterative] O(1) space
// Worst: O(n) time | [recursive] O(n) space | [iterative] O(1) space

// Recursive Solution
const findClosestValueInBst = (tree, target) => {
  
	let smallestDifference = Infinity
	let closestNumber = null
	
	const checkNode = (node) => {
		// Check difference between target and node's value
		let difference = Math.abs(target - node.value)
		// If value is the closest, update smallestDifference and closestNumber
		if (difference < smallestDifference) {
			smallestDifference = difference
			closestNumber = node.value
		}
		// Recursively check right
		if (node.right && node.value < target) checkNode(node.right)
		// Recursively check left
		else if (node.left && node.value > target) checkNode(node.left) 
	}
	
	checkNode(tree)
	return closestNumber
	
}