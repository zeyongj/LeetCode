#include <stdio.h>

/* Function to find median of two sorted arrays */
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0, m1 = -1, m2 = -1;
    for (int count = 0; count <= (nums1Size + nums2Size) / 2; count++) {
        if (i != nums1Size && j != nums2Size) {
            if (nums1[i] < nums2[j]) {
                m1 = m2;
                m2 = nums1[i++];
            } else {
                m1 = m2;
                m2 = nums2[j++];
            }
        } else if (i != nums1Size) {
            m1 = m2;
            m2 = nums1[i++];
        } else {
            m1 = m2;
            m2 = nums2[j++];
        }
    }
    return (nums1Size + nums2Size) % 2 == 0 ? (m1 + m2) / 2.0 : m2;
}
