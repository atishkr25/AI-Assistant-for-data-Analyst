# PROJECT SYNOPSIS

## 1. PROJECT IDENTIFICATION
- **Project Title:** AI Data Analyst Assistant: Conversational Tabular Analytics & Autonomous Visualization
- **Project ID:** P_123
- **Suggested Repository Name:** `AI-Assistant-for-data-Analyst`
- **GitHub Repository URL:** `https://github.com/atishkr25/AI-Assistant-for-data-Analyst`
- **Domain:** Artificial Intelligence, Natural Language Processing (NLP), Data Analytics, Business Intelligence
- **Primary Technologies:** Python, Streamlit, Groq Cloud (Llama-3.3-70b-versatile), Pandas, Seaborn, Matplotlib

---

## 2. ABSTRACT / EXECUTIVE SUMMARY
Extracting swift, meaningful insights from tabular business documents (CSV, Excel spreadsheets, JSON records) is an indispensable necessity across enterprise workflows. However, non-technical stakeholders are often restricted by complex Pandas or SQL syntax requirements, creating a persistent dependency on data engineers and analysts.

The **AI Data Analyst Assistant** is an interactive, web-based analytical application built with Streamlit, Groq Cloud (Llama-3.3-70B), Pandas, and Seaborn. The system accepts diverse structured formats (CSV, XLSX, XLS, JSON), instantly computes data quality summaries (total rows, columns, duplicate records, missing values), and provides one-click autonomous data hygiene tools. Through an intuitive conversational AI chat interface, users express inquiries in natural language; the system dynamically translates queries into optimized Python code, executes it in a sandboxed runtime, and renders publication-ready Seaborn and Matplotlib visualizations.

---

## 3. PROBLEM STATEMENT
- **Technical Barrier to Querying:** Non-technical operators lack programming fluency in Pandas and Matplotlib, slowing down routine business exploration.
- **Data Hygiene Bottlenecks:** Raw file exports often contain duplicates and null records that distort statistical analysis.
- **Inference Latency:** Traditional cloud LLMs suffer from high latency, creating sluggish user conversational experiences.
- **Format Inflexibility:** Many analysis tools strictly accept single CSV files, failing to handle modern Excel spreadsheets or nested JSON structures.

---

## 4. OBJECTIVES
- **Conversational Data Interaction:** Enable natural-language exploratory analysis across CSV, Excel, and JSON datasets.
- **Autonomous Data Cleaning:** Provide single-click tools to purge duplicate entries and impute missing cells.
- **Ultra-Low-Latency Inference:** Leverage Groq Language Processing Units (LPUs) running Llama-3.3-70b for sub-second code generation.
- **Automated Statistical Visualizations:** Render publication-ready bar charts, correlation heatmaps, and scatter plots using Seaborn and Matplotlib.
- **Session Memory:** Maintain chat history to support iterative, contextual analytical discussions.

---

## 5. SYSTEM ARCHITECTURE & DATA FLOW
1. **Ingestion & Profiling:** Files (CSV, XLSX, JSON) are parsed into an in-memory DataFrame; dimensions and quality metrics are computed.
2. **Autonomous Cleaning:** User triggers duplicate removal or missing value imputation with immediate feedback alerts.
3. **Conversational Synthesis:** User prompts are contextualized with dataset columns and sent to Groq Llama-3.3.
4. **Sandboxed Code Execution:** Generated Python code runs locally within an isolated execution dictionary.
5. **Visual Output:** Results are presented as markdown text, tabular views, and rendered Seaborn figures.

---

## 6. KEY FUNCTIONAL MODULES
- **Data Ingestion & Hub:** Parses CSV, Excel (.xlsx, .xls), and JSON payloads into Pandas DataFrames.
- **Data Overview Engine:** Computes real-time metric cards for rows, columns, duplicates, and missing values.
- **One-Click Cleaning Tools:** Provides interactive de-duplication and null value imputation.
- **Groq Llama-3.3 Inference Client:** Translates natural language questions into Python data analysis scripts.
- **Execution & Plotting Engine:** Evaluates code and visualizes distributions, correlations, and aggregations using Seaborn & Matplotlib.

---

## 7. TECHNICAL SPECIFICATIONS
- **Frontend / UI:** Streamlit 1.37+
- **Data Processing:** Pandas 2.0+, NumPy
- **Inference Engine:** Groq Cloud (Llama-3.3-70b-versatile)
- **Data Visualization:** Seaborn, Matplotlib
- **Document Deserialization:** openpyxl, xlrd, json
- **Configuration:** python-dotenv

---

## 8. FUTURE ENHANCEMENTS
- Advanced statistical imputation (mean, median, KNN) and automated outlier detection.
- Multi-table relational merging with automatic join inference.
- One-click exportable PDF / DOCX executive discovery reports.

