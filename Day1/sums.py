class Sums:

    @staticmethod
    def find_sum(target, ylist, entry_count):
        if entry_count == 2:
            for i in range(len(ylist)):
                for j in range(i + 1, len(ylist)):
                    if ylist[i] + ylist[j] == target:
                        return ylist[j], ylist[i], ylist[i] * ylist[j]
        else:
            for i in range(len(ylist)):
                for j in range(i + 1, len(ylist)):
                    for k in range(j + 1, len(ylist)):
                        if ylist[i] + ylist[j] + ylist[k] == target:
                            return ylist[i], ylist[j], ylist[k], ylist[i] * ylist[j] * ylist[k]
