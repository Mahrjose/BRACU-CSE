# Problem -05


class FinalQ:
    def print(self, array, idx):
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            print(f"{idx+1}. Investment: {array[idx]}; Profit: {profit}")
            self.print(array, idx + 1)

    def calcProfit(self, investment):
        if investment <= 25000:
            return 0.0

        elif investment <= 100000:
            return 45 + self.calcProfit(investment - 1000)

        elif investment > 100000:
            return 80 + self.calcProfit(investment - 1000)

        else:
            return 0


print("\nNo. 5-->")
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)
