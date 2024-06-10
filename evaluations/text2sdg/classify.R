# Load text2sdgs
library("text2sdg")

# Load manipulation libraries
library(dplyr)
library(tidyr)
library(purrr)

# Load benchmark
benchmark <- read.csv("benchmark.csv", header=TRUE)
texts <- benchmark[["text"]]

# Identify SDGs
hits <- detect_sdg(texts)

# Extract SDG numbers from text
extracted <- hits %>% extract(sdg, c("predicted_sdg"), "SDG-0?(\\d+)")

# Group by document
grouped <- extracted %>% group_by(document) %>% summarise(predicted_sdgs=paste(predicted_sdg, collapse=", "))

# Merge with benchmark
benchmark$row_id <- as.integer(rownames(benchmark))
results <- merge(benchmark, grouped, by.x = "row_id", by.y = "document", all.x = TRUE, sort = FALSE)

# Sort by row ID
results <- results[order(results$row_id), ]

# Keep desired columns only
results <- subset(results, select = c(id, text, predicted_sdgs))

# Write results
write.csv(results, "/predictions.csv", row.names=FALSE)