# Research Decisions Log

*   **Review topic and key papers:** Single LLM versus Multi-Agent Debate Systems[cite: 12]. Key papers: Du et al. (2023), Wynn et al. (2025)[cite: 12].
*   **Research gap:** Homogeneous multi-agent debate systems are susceptible to sycophancy, conformity, and premature consensus[cite: 12, 17].
*   **Research question:** Does assigning distinct, adversarial personas (e.g., "optimist," "skeptic," "domain expert") reduce sycophancy and premature consensus compared to homogeneous agent debate?[cite: 17].
*   **Study pathway:** Targeted modification. Changing one component of a baseline (system prompts)[cite: 2].
*   **Primary metric and control:** Semantic similarity via Sentence-BERT (metric) holding the LLM model and generation temperature constant (control).
*   **Computing and risks:** Google Gemini Free Tier API. Risk of rate limits handled via Python `time.sleep()` calls.