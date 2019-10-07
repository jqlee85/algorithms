// O(n) time | O(n) space
const waterArea = (heights) => {
      
      // Get left maxes
      let leftMaxes = []
      let leftMax = 0
      heights.forEach((height,i)=>{
          if (height > leftMax) leftMax = height
          leftMaxes[i] = leftMax
      })
      
      // Get right maxes
      let rightMaxes = []
      let rightMax = 0
      for (let i = heights.length - 1; i >= 0; i--) {
          if (heights[i] > rightMax) rightMax = heights[i]
          rightMaxes[i] = rightMax
      }
      
      // Get water depths
      let waterVolume = 0
      heights.forEach((height,i)=>{
          let minBarrier = (rightMaxes[i] < leftMaxes[i]) ? rightMaxes[i] : leftMaxes[i]
          if (height < minBarrier) waterVolume += minBarrier - height
      })
      
      return waterVolume
      
  }
  
  // Do not edit the line below.
  exports.waterArea = waterArea;
  