// Average: O(logn) time | [recursive] O(logd) space (d = depth of BST) | [iterative] O(1) space
// Worst: O(n) time | [recursive] O(n) space | [iterative] O(1) space

// Recirsive Solution
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
		// If difference is zero, return null													 
		if (difference === 0)	return null																 
		// Else check left and right nodes
		else {
			// Is value smaller than the target
			let valueSmaller = node.value < target
			// Recursively check left
			if (node.left && !valueSmaller) checkNode(node.left) 
			// Recursively check right
			if (node.right && valueSmaller) checkNode(node.right)
		}	
	}
	
	checkNode(tree)
	return closestNumber
	
}

// Do not edit the line below.
exports.findClosestValueInBst = findClosestValueInBst;
