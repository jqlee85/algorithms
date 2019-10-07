// Best: O(n) time | O(1) space
// Average: O(n^2) time | O(1) space
// Worst: O(n^2) time | O(1) space
function insertionSort(array) {
	if (array.length < 2) return array
	for (let i=1; i < array.length; i++) {
		let current = array[i]
		let j = i-1
		let currentIsLess = true
		while (currentIsLess && j >= 0) {
			let compareVal = array[j]
			// If current value is than compareVal, end loop
			if (current >= compareVal) {
				currentIsLess = false
			} else {
				// Move compareVal right and replace with current
				array[j+1] = compareVal
				array[j] = current
 			}
			j--
		}
	}
	return array
}

// Do not edit the line below.
exports.insertionSort = insertionSort;
