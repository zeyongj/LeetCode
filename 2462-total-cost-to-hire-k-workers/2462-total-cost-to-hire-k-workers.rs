import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {

	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h IntHeap) Top() int {
	return h[0]
}

func totalCost(costs []int, k int, candidates int) int64 {
	i, j := 0, len(costs)-1
	ans := int64(0)
	upPq := &IntHeap{}
	downPq := &IntHeap{}
	heap.Init(upPq)
	heap.Init(downPq)
	for i < j && candidates > 0 {
		heap.Push(downPq, costs[i])
		heap.Push(upPq, costs[j])
		i++
		j--
		candidates--
	}
	if i == j && candidates > 0 {
		heap.Push(downPq, costs[i])
		i++
	}
	for k > 0 {
		if upPq.Len() == 0 {
			ans += int64(heap.Pop(downPq).(int))
		} else if downPq.Len() == 0 {
			ans += int64(heap.Pop(upPq).(int))
		} else {
			if upPq.Top() < downPq.Top() {
				ans += int64(heap.Pop(upPq).(int))
				if j >= i {
					heap.Push(upPq, costs[j])
					j--
				}
			} else {
				ans += int64(heap.Pop(downPq).(int))
				if i <= j {
					heap.Push(downPq, costs[i])
					i++
				}
			}
		}
		k--
	}
	return ans
}