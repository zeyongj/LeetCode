class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        net_wait_time = 0

        for customer in customers:
            # The next idle time for the chef is given by the time of delivery
            # of current customer's order.
            next_idle_time = max(customer[0], next_idle_time) + customer[1]

            # The wait time for the current customer is the difference between
            # his delivery time and arrival time.
            net_wait_time += next_idle_time - customer[0]

        # Divide by total customers to get average.
        average_wait_time = net_wait_time / len(customers)
        return average_wait_time