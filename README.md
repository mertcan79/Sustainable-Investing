# Sustainable Investing

Portfolio management is changing to be a multi objective problem because investors are putting other parameters in the equation such as the sustainability of the asset. 
These investors believe how they allocate their capital is one of the most powerful tools for addressing the sustainability challenges of our planet.

# Objective

The main objective is to pick companies to invest in out of the database of companies using multi objective optimization. 

There are different objectives, namely: 
Maximize expected return.
Maximize environmental, social, and corporate sustainability.
Maximize dividend yield.
Maximize clean energy use.

Pyomo is used for the multiobjective optimization. GLTK installation is necessary. 

# Data

Companies and related parameters such as return and clean energy usage are scrapped through the web. It consists of 361 companies with mentioned features.  

# Output

The selected companies from our algorithm are as follows:


Companies to invest in:
 Aegon NV 0.05
 American Airlines Group Inc 0.05
 Banco Santander Brasil SA 0.05
 Banco Santander Chile 0.00845426457548186
 British American Tobacco PLC 0.05
 Eni SpA 0.05
 Fabege AB 0.05
 Grupo Aval Acciones y Valores SA 0.05
 Honda Motor Co Ltd 0.05
 Jefferies Financial Group Inc 0.05
 Johnson Controls International plc 0.05
 Lloyds Banking Group PLC 0.05
 Mizuho Financial Group Inc 0.05
 POSCO 0.05
 Sasol Ltd 0.05
 SK Telecom Co Ltd 0.05
 Teck Resources Ltd 0.05
 Telefonica Brasil SA 0.05
 Ultrapar Participacoes SA 0.05
 Vedanta Ltd 0.0415457354245179
 WPP PLC 0.05
 
Total weight 1.0

# Future Work
1. An improved epsilon constraint-handling mechanism can be further implemented, which combines it with a decomposition-based multi-objective evolutionary algorithm (MOEA/D). 
It adjusts the epsilon level dynamically according to the ratio of feasible to total solutions (RFS) in the current population 
2. Weight optimization
