

# Percolation
This project was originally inspired by the video <a href="https://www.youtube.com/watch?v=a-767WnbaCQ">Percolation: a Mathematical Phase Transition</a> by <b>Spectral Collective</b>.

Percolation theory fundamentally revolves around a simple way to model phase transitions mathematically. On a percolated graph, the probability that any given edge between two nodes is 'open' is known as the p-value. From this simple rule, surprisingly complex emergent behaviours can be observed when examining the effects of various  p-values on an n-dimensional grid.

One notable observation is that each model of percolation will display a 'critical value', where a distinct phase transition can be observed. For a traditional two-dimensional square lattice, the critical value is known to be at p=0.5.

* The probability of an infinite cluster existing when the p-value is less than or equal to the critical value is <b>always</b> 0 (impossible)
* Likewise, the probability of one existing when the p-value is greater than the critical value is <b>always</b> 1 (certain)

Within the context of two-dimensional grid lattices, it is also known that there will be exactly one infinite cluster, and no more.

<div align="center">
<img src="https://raw.githubusercontent.com/jaredlandau/Percolation/main/percolation.gif" alt="drawing" width="500"/>
<p><i>Percolation graph of n=500, with the p-value ranging from 0.35 to 0.65. A phase transition is clearly visible at p=0.5 as predicted.</i></p>
</div>

Percolation theory is still relatively poorly understood in the context of mathematics, particularly when exploring grids of three or more dimensions. If a formula for calculating the critical value does exist (which is an ongoing topic of debate), it has not yet been found. Currently, critical values in more complex scenarios can only be derived by conducting numerical simulations.

## References
* <a href="https://www.youtube.com/watch?v=a-767WnbaCQ">Percolation: a Mathematical Phase Transition</a>
* <a href="https://en.wikipedia.org/wiki/Percolation_theory">Percolation theory</a>