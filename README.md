🌦️ Real-Time Weather Intelligence Platform
A serverless, event-driven weather monitoring system built on Microsoft Azure that ingests live weather data, processes it in real-time, and delivers actionable insights through interactive dashboards and automated alerts.

📋 Overview
This project demonstrates end-to-end real-time data engineering using Azure's modern data stack. The pipeline ingests weather data from external APIs, streams it through Event Hub, processes it using Microsoft Fabric and Azure Databricks, stores it in Kusto DB for fast analytical queries, and visualizes it in Power BI with sub-minute refresh rates.

Key Highlights

-Real-time data ingestion with sub-minute latency
-Scalable serverless architecture
-Automated alerting for extreme weather conditions
-Interactive dashboards with live refresh

What I'd Do Differently
If I rebuilt this project:

Start with Azure Functions + Event Hub for ingestion from day one
Use Databricks only for the transformation layer, not ingestion
Set up budget alerts in Azure Cost Management immediately
Use spot instances for non-production Databricks clusters

✨ Features
Real-Time Ingestion

Azure Function triggers every 2 minutes to fetch weather data
Handles multiple cities/regions in parallel
Implements retry logic with exponential backoff for API reliability
Pushes events to Event Hub in JSON format

Data Transformation

Cleaning: Null handling, data type standardization
Enrichment: Adds location metadata, timezone conversion
Aggregation: Rolling averages, min/max calculations
Unit Conversion: Celsius/Fahrenheit, km/h to mph

Analytics & Storage

Kusto DB optimized for time-series weather queries
Retention policies for hot/warm/cold data tiers
Pre-aggregated tables for dashboard performance