/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var maxNumEdgesToRemove = function(n, edges) {
    // UnionFind class definition
    class UnionFind {
        constructor(n) {
            this.representative = Array.from({ length: n + 1 }, (_, index) => index);
            this.componentSize = Array.from({ length: n + 1 }, () => 1);
            this.components = n;
        }

        findRepresentative(x) {
            if (this.representative[x] === x) {
                return x;
            }
            this.representative[x] = this.findRepresentative(this.representative[x]);
            return this.representative[x];
        }

        performUnion(x, y) {
            x = this.findRepresentative(x);
            y = this.findRepresentative(y);

            if (x === y) {
                return 0;
            }

            if (this.componentSize[x] > this.componentSize[y]) {
                this.componentSize[x] += this.componentSize[y];
                this.representative[y] = x;
            } else {
                this.componentSize[y] += this.componentSize[x];
                this.representative[x] = y;
            }

            this.components--;
            return 1;
        }

        isConnected() {
            return this.components === 1;
        }
    }

    // Main function logic
    let alice = new UnionFind(n);
    let bob = new UnionFind(n);

    let edgesRequired = 0;

    for (let edge of edges) {
        if (edge[0] === 3) {
            edgesRequired += (alice.performUnion(edge[1], edge[2]) | bob.performUnion(edge[1], edge[2]));
        }
    }

    for (let edge of edges) {
        if (edge[0] === 2) {
            edgesRequired += bob.performUnion(edge[1], edge[2]);
        } else if (edge[0] === 1) {
            edgesRequired += alice.performUnion(edge[1], edge[2]);
        }
    }

    if (alice.isConnected() && bob.isConnected()) {
        return edges.length - edgesRequired;
    }

    return -1;
};