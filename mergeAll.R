#!/usr/bin/env Rscript

#mergeAll.R



# Load BLAST results as a table using tab (\t) as separator.

# There is no header with column names, so set header=FALSE

blast <- read.table("../BLAST/alignPredicted.txt", sep="\t", header=FALSE, fill=TRUE)



# Set column names to match fields selected in BLAST

colnames(blast) <- c("qseqid", "sacc", "qlen", "slen", "length", "nident", "pident", "evalue", "stitle")

# Calculate the coverage as nident/slen

blast$cov <- blast$nident/blast$slen



# Select only blast rows where coverage is greater than .9

blast <- subset(blast, cov > .9, select=-c(stitle))



# Read kegg.txt, produced by get_kegg_ids, as a table

kegg <- read.table("kegg.txt", sep="\t", header=FALSE, fill= TRUE)



# Set the column names for kegg

colnames(kegg) <- c("sacc", "kegg")



# Remove the up: prefix from the accession number so it will match the BLAST

# subject accession (sacc)

kegg$sacc <- gsub("up:", "", kegg$sacc)



# Merge the tables. Since one column name in common, just give

# the two tables as parameters to merge.

blast_kegg <- merge(blast, kegg)



# Display the first few lines of output

head(blast_kegg)

go<- read.csv ("sp_go.txt",sep="\t", header=FALSE, fill=TRUE)
colnames(go) <- c ("sacc","go")
head (go)
blastkegg_go <- merge (blast_kegg,go)

# Reading table from text file

kegg <- read.table("kegg.txt", sep = "\t", header=FALSE, fill=TRUE)

# Setting column name

colnames(kegg) <- c("sacc","kegg")



ko <- read.table("ko.txt", sep="\t", header=FALSE, fill=TRUE)

colnames(ko) <- c("kegg", "ko")

path <- read.table("path.txt", sep="\t", header=FALSE, fill=TRUE)

colnames(path) <- c("ko", "path")

getPath <- read.table("ko", sep="\t", header=FALSE, fill=TRUE)

colnames(getPath) <- c("path", "Pathway")



# Merged variables of all text files

kegg_ko <- merge(kegg, ko)

ko_path <- merge(kegg_ko, path)

pathway <- merge(ko_path, getPath)




head(pathway)


