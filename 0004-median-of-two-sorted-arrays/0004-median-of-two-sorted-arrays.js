/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
function findMedianSortedArrays(nums1, nums2) {
    let i = 0, j = 0, m1 = -1, m2 = -1;
    for (let count = 0; count <= (nums1.length + nums2.length) / 2; count++) {
        if (i !== nums1.length && j !== nums2.length) {
            if (nums1[i] < nums2[j]) {
                m1 = m2;
                m2 = nums1[i++];
            } else {
                m1 = m2;
                m2 = nums2[j++];
            }
        } else if (i !== nums1.length) {
            m1 = m2;
            m2 = nums1[i++];
        } else {
            m1 = m2;
            m2 = nums2[j++];
        }
    }
    return (nums1.length + nums2.length) % 2 === 0 ? (m1 + m2) / 2 : m2;
}