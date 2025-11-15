data = f"""
=== Graph 88 ===
Depth: 3
Number of reactions: 3
Precursor cost: 19
Atom economy: 58.94%
Target: CCOC(=O)c1ccc(N)cc1

Reaction steps:

  Step 1:
  Product: CCOC(=O)c1ccc(N)cc1
  Reactants: ['CCOC(=O)c1ccc(N=[N+]=[N-])cc1']

  Step 2:
  Product: CCOC(=O)c1ccc(N=[N+]=[N-])cc1
  Reactants: ['CC=[N+]=[N-]', '[N-]=[N+]=Nc1ccc(C(=O)O)cc1']

  Step 3:
  Product: CC=[N+]=[N-]
  Reactants: ['CCN(N=O)C(N)=O']

Nodes by depth:
  Depth 0: 1 nodes
  Depth 1: 1 nodes
  Depth 2: 1 nodes
  Depth 3: 1 nodes
  Depth 4: 2 nodes
  Depth 5: 1 nodes
  Depth 6: 1 nodes

=== Graph 89 ===
Depth: 3
Number of reactions: 3
Precursor cost: 5.39
Atom economy: 28.85%
Target: CCOC(=O)c1ccc(N)cc1

Reaction steps:

  Step 1:
  Product: CCOC(=O)c1ccc(N)cc1
  Reactants: ['CCOC(=O)c1ccc(N=C(c2ccccc2)c2ccccc2)cc1']

  Step 2:
  Product: CCOC(=O)c1ccc(N=C(c2ccccc2)c2ccccc2)cc1
  Reactants: ['CCOC(=O)c1ccc(OS(=O)(=O)C(F)(F)F)cc1', 'N=C(c1ccccc1)c1ccccc1']

  Step 3:
  Product: CCOC(=O)c1ccc(OS(=O)(=O)C(F)(F)F)cc1
  Reactants: ['CCOC(=O)c1ccc(O)cc1', 'O=S(=O)(Nc1ccccc1)C(F)(F)F']
"""

message = f"""
Evaluate the greeness of the following process, step by step, output in yaml.

{data}

"""

sample_output = """
graph_88:
  target: "CCOC(=O)c1ccc(N)cc1"
  overall:
    depth: 3
    steps: 3
    precursor_cost: 19
    atom_economy_percent: 58.94
    greenness_summary: "Poor to moderate — high precursor cost, use of hazardous diazonium/azide-like intermediates and N-oxide reagents, multiple steps with potential safety and waste concerns."
  step_evaluation:
    - step: 1
      reaction: "CCOC(=O)c1ccc(N=[N+]=[N-])cc1 -> CCOC(=O)c1ccc(N)cc1"
      concerns:
        - "Reduction of a diazonium/azo-type intermediate likely requires reductant or hydrogenation — potential use of heavy metals or stoichiometric reducing agents."
        - "Possible formation of N2 gas ( benign ) but workup may produce inorganic salts or metal residues."
      green_score: 3/10
      recommendations:
        - "Prefer catalytic hydrogenation with recyclable catalyst if safe; avoid stoichiometric reductants."
    - step: 2
      reaction: "CC=[N+]=[N-] + [N-]=[N+]=Nc1ccc(C(=O)O)cc1 -> CCOC(=O)c1ccc(N=[N+]=[N-])cc1"
      concerns:
        - "Use of diazo/azide-like coupling between two highly reactive nitrogen species — substantial safety (explosion/thermal) risk."
        - "Likely generates inorganic salts or strong acids/bases during coupling."
      green_score: 2/10
      recommendations:
        - "Avoid routes that require handling multiple diazo/azide species; consider alternative electrophile/nucleophile pairs or safer diazotization conditions at low temp."
    - step: 3
      reaction: "CCN(N=O)C(N)=O -> CC=[N+]=[N-]"
      concerns:
        - "Generation of a diazo/azide equivalent from N‑oxide or nitrosated amine involves potentially toxic nitrosating agents (e.g., NaNO2/HCl) and can form hazardous byproducts."
        - "Thermal instability and explosion risk for small diazo compounds."
      green_score: 1/10
      recommendations:
        - "Replace with alternative nitrogen-transfer that avoids generating free diazo species; consider direct amine functionalization or use of protected aminating reagents."
  major_green_flags:
    - "High safety hazards from diazo/azide chemistry and nitrosation steps."
    - "Likely high waste from stoichiometric reagents and possible heavy‑metal catalysts for reduction."
  minor_green_flags:
    - "Moderate atom economy (58.9%) but poor precursor cost (19)."
    - "Several steps produce small unstable intermediates increasing risk and complexity."
  suggested_alternatives:
    - "Use classical electrophilic aromatic substitution (e.g., nitration → catalytic reduction → acylation) if compatible, or convert a nitro substituted precursor to aniline via catalytic hydrogenation from a stable nitroarene."
    - "Design route avoiding diazo/azide intermediates; use safer aminating reagents or C–N bond forming cross-coupling (Buchwald–Hartwig) from aryl halide precursors."

graph_89:
  target: "CCOC(=O)c1ccc(N)cc1"
  overall:
    depth: 3
    steps: 3
    precursor_cost: 5.39
    atom_economy_percent: 28.85
    greenness_summary: "Moderate to poor — lower precursor cost and avoids highly hazardous diazo chemistry, but very low atom economy and use of perfluoroalkyl sulfonyl reagents (PFAS-like) and likely stoichiometric activating groups increase environmental impact."
  step_evaluation:
    - step: 1
      reaction: "CCOC(=O)c1ccc(N=C(c2ccccc2)c2ccccc2)cc1 -> CCOC(=O)c1ccc(N)cc1"
      concerns:
        - "Hydrolysis or hydrogenolysis of a diaryl imine/Schiff-type linkage may require acid or hydrogenation; byproducts include diaryl fragments or require excess reagents."
      green_score: 4/10
      recommendations:
        - "Use catalytic hydrogenation under mild conditions or hydrolytic cleavage with recyclable acid catalysts."
    - step: 2
      reaction: "CCOC(=O)c1ccc(OS(=O)(=O)C(F)(F)F)cc1 + N=C(c1ccccc1)c1ccccc1 -> CCOC(=O)c1ccc(N=C(c2ccccc2)c2ccccc2)cc1"
      concerns:
        - "Formation of a diaryl imine via nucleophilic substitution likely uses strong conditions; the other reactant is a bulky diaryl imine precursor."
        - "Use of sulfonyl-activated phenol suggests firing off a leaving group — the sulfonyl reagent is perfluoroalkylated (PFAS-like), persistent and environmentally problematic."
      green_score: 3/10
      recommendations:
        - "Avoid trifluoromethyl/perfluoroalkyl sulfonyl activating groups; use tosylates/mesylates or catalytic coupling methods (e.g., C–N cross-coupling) to install aryl amine."
    - step: 3
      reaction: "CCOC(=O)c1ccc(O)cc1 + O=S(=O)(Nc1ccccc1)C(F)(F)F -> CCOC(=O)c1ccc(OS(=O)(=O)C(F)(F)F)cc1"
      concerns:
        - "Use of N‑sulfonylating reagent bearing C(F)3 group introduces persistent perfluoroalkyl substances; likely stoichiometric bases and solvent use; generates sulfonamide byproducts."
        - "Low atom economy due to installation and later removal of activating group."
      green_score: 2/10
      recommendations:
        - "Replace perfluoroalkyl sulfonylating reagent with non‑PFAS activator (e.g., tosyl chloride) or use catalytic activation (transition-metal catalyzed C–O activation) to avoid persistent pollutants."
  major_green_flags:
    - "Use of perfluoroalkyl sulfonyl (PFAS-like) reagents — environmental persistence and regulatory concern."
    - "Very low atom economy (28.9%) indicating large waste generation."
  minor_green_flags:
    - "Multiple steps likely require stoichiometric activating reagents and solvent-intensive workups."
  suggested_alternatives:
    - "Consider direct C–N bond formation via Buchwald–Hartwig amination of an aryl halide starting material (higher atom economy, catalytic conditions)."
    - "Use non‑PFAS leaving groups (tosyl/mesyl) or catalytic activation methods to minimize persistent contaminants and waste."
"""