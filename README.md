# QOC-Problem
An attempt at quantum tic-tac-toe

For this project, I explored the question of quantum tic-tac-toe more generally. I've created a few different solutions attempts that illucidate different interesting things I've learned. I've made an object oriented approach that visualizes the game board and attempts to make use of the symmetry of the board to reduce the dimensionality of the space. The attached excel file illustrates how under rotational transformation, sets of different states (as lists of qubits) all map to the same game board. It should be possible to reduce this problem to 6 qubits or using a turn by turn network based approached even further reductions may be posssible. The QOC file is a quantum attempt, where each remaining square maps to qubit in Hilbert space that expands by tensor product to occupy the whole board. There are some normalization issues that I have not rectified, as well as some assumptions such as opponent random play that could be relaxed in later versions. I'll continue to update this problem, I want to idealize this with a symmetric reduction and decomposition to standard (Hadamard, Pauli etc.) gates and create the quantum circuit needed to play.

This has been an interesting problem and I've enjoyed the opportunity. I'm a passionate researcher and very interested in working on a quantum information based research project.

Thanks for your consideration.

- Matt
