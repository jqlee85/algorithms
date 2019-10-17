// Best: O(n^2) time | O(1) space
// Average: O(n^2) time | O(1) space
// Worst: O(n^2) time | O(1) space
const selectionSort = (array) => {
	
	// Gets index of smallest unsorted value
	const getSmallestUnsortedIdx = (startIdx) => {
		let smallestIdx = startIdx
		for (let j = startIdx;j<array.length;j++) {
			if (array[j] < array[smallestIdx]) smallestIdx = j
		}
		return smallestIdx
	}
	
	for (let i=0;i<array.length;i++) {
		// Find smallest unsorted element
		let smallestIdx = getSmallestUnsortedIdx(i)
		// Swap smallest unsorted value with first unsorted value
		let firstUnsorted = array[i]
		array[i] = array[smallestIdx]
		array[smallestIdx] = firstUnsorted
	}
	
	return array
	
}

// Do not edit the line below.
exports.selectionSort = selectionSort;
