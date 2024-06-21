class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        unrealized_customers = 0

        # Calculate initial number of unrealized customers in first 'minutes' window
        for i in range(minutes):
            unrealized_customers += customers[i] * grumpy[i]

        max_unrealized_customers = unrealized_customers

        # Slide the 'minutes' window across the rest of the customers array
        for i in range(minutes, n):
            # Add current minute's unsatisfied customers if the owner is grumpy
            # and remove the customers that are out of the current window
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]

            # Update the maximum unrealized customers
            max_unrealized_customers = max(
                max_unrealized_customers, unrealized_customers
            )

        # Start with maximum possible satisfied customers due to secret technique
        total_customers = max_unrealized_customers

        # Add the satisfied customers during non-grumpy minutes
        for i in range(n):
            total_customers += customers[i] * (1 - grumpy[i])

        # Return the maximum number of satisfied customers
        return total_customers