class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num_stations = len(gas)
        tank_amount = gas_used = cost_paid = start = 0

        for i in range(num_stations):
            gas_used += gas[i]
            cost_paid += cost[i]
            tank_amount += gas[i] - cost[i]
            # If the tank runs out, we started too early
            if tank_amount < 0:
                tank_amount = 0
                start = i+1
        
        return -1 if cost_paid > gas_used else start