// Implement dynamic programming solution for O(nd) solution
// O(nd) time [d = lenth of denoms] | O(n) space [creating minCoins array for all values up to n]
function minNumberOfCoinsForChange(n, denoms) {
	
	// Initialize minNumbers array for every target value up to n
	let minCoins = Array(n+1).fill(Infinity)
	minCoins[0] = 0
	
	// Loop through each denomination, and each target value, setting new minimum number of coins needed for that value
	denoms.forEach((denom,i)=>{
		minCoins.forEach((current,target)=>{
			if ( denom <= target ) {
				let remainder = target - denom
				let numCoins = 1 + minCoins[remainder]
				if (numCoins < current) minCoins[target] = numCoins
			}
		})
	})

	return (minCoins[n] !== Infinity) ? minCoins[n] : -1

}

// Do not edit the line below.
exports.minNumberOfCoinsForChange = minNumberOfCoinsForChange;
