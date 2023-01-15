class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m > n) { 
            int[] temp = nums1; nums1 = nums2; nums2 = temp;
            int temp2 = m; m = n; n = temp2;
        }
        int i, j, imin = 0, imax = m, half = (m + n + 1) / 2;
        while (imin <= imax) {
            i = (imin + imax) / 2;
            j = half - i;
            if (i < m && nums2[j-1] > nums1[i])
                imin = i + 1;
            else if (i > 0 && nums1[i-1] > nums2[j])
                imax = i - 1;
            else {
                double maxLeft;
                if (i == 0) maxLeft = nums2[j-1];
                else if (j == 0) maxLeft = nums1[i-1];
                else maxLeft = Math.max(nums1[i-1], nums2[j-1]);
                if ((m + n) % 2 == 1) return maxLeft;

                double minRight;
                if (i == m) minRight = nums2[j];
                else if (j == n) minRight = nums1[i];
                else minRight = Math.min(nums1[i], nums2[j]);

                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
}
