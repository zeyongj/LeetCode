class Solution:
    def mostPopularCreator(self, creators, ids, views):
        pop = Counter()
        most = {}
        most_views = 0
        for creator, id, view in zip(creators, ids, views):
            pop[creator] += view
            most_views = max(most_views, pop[creator])
            if creator not in most or view > most[creator][1] or (view == most[creator][1] and id < most[creator][0]):
                most[creator] = [id, view]
        
        return [[creator, most[creator][0]] for creator, view in pop.items() if view == most_views]