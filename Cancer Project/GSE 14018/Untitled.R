install.packages(c("limma" , "pheamap" , "ggplot2",  "reshape2" , "plyr" , "biobase"))

library(dplyr)
library(limma)
library(pheatmap)
library(gplots)
library(ggplot2)
library(reshape2)
library(plyr)
library(gdata)
library(venndiagram)

setwd("~/Documents/Bioinformatics - R/main")

ex  <- read.delim("Data/GSE14018_series_matrix.txt", comment.char = "!")
plt <- read.delim("Data/GPL96.annot")
plt <- data.frame(ID = plt$ID , symbol = sub("///.*" , "", plt$Gene.symbol))

library(dplyr)
plt <- distinct(plt, symbol, .keep_all = TRUE)

ex  <- merge(plt, ex, by.x = "ID" , by.y = "ID_REF") 


rownames(ex) <- ex$symbol
ex <- ex[ , -1 : -2]

###ex <- subset(ex, select = -c(brain18, brain8, lung36, lung30, lung1, lung2, lung17, liver7, liver14, liver27, bone25, bone19, bone12))
gr <- c("lung" , "lung", "lung", "liver", "brain", "lung", "liver", "brain", "lung", "brain", "lung", "bone", "lung", "liver",
        "lung", "liver", "lung", "brain", "bone", "brain", "bone", "brain", "brain", "bone", "bone", "lung", "liver", "lung", "bone",
        "lung", "lung", "liver", "bone", "lung", "lung", "lung")
gr1 <- paste0(gr, seq_along(gr))
colnames(ex) <- gr1


###over_simplification_problem
ex <- log2(ex + 1)

###now we shoul controll our quality control(optional)
library(limma)
boxplot1 <- normalizeQuantiles(ex)

pdf("~/Documents/Bioinformatics - R/Main/Results/Boxplotnormal normal.pdf" ,width=17, height = 17)
boxplot(ex)
dev.off()

#install.packages('systemfonts')
#systemfonts :: match_font("SF Pro Text")

###corelation Heatmap
library(pheatmap)
library(gplots)
pdf("~/Documents/Bioinformatics - R/Main/Results/Haetmap normal212.pdf", width = 11, height= 11)
pheatmap(cor(ex), labels_row = gr1, labels_col = gr1, color = colorRampPalette(c("navy", "black", "orange"))(50), border_color = "NA" )
dev.off()


###principle componenet analysis
#install.packages("devtools")
pc <- prcomp(ex)
pdf("~/Documents/Bioinformatics - R/Main/Results/PCA.pdf", width = 17, height= 17)
plot(pc)
plot(pc$x[, 1:2])
dev.off()

library(ggplot2)
PCR <- data.frame(pc$r[, 1:2], Group = gr)
pdf("~/Documents/Bioinformatics - R/Main/Results/PCR modified.pdf", width = 10, height= 8)
ggplot (PCR,aes(PC1, PC2, color = gr)) + geom_point(size = 3) + theme_bw()
ggplot (PCR,aes(PC1, PC2, label = gr1)) + geom_text(size = 3) + theme_bw()
dev.off()

ex <- subset(ex, select = -c(brain18, brain8, lung36, lung30, lung1, lung2, lung17, liver7, liver14, liver27, bone25, bone19, bone12))
gr <- c("lung", "liver", "brain", "lung",  "lung", "brain",
        "lung", "lung",  "lung", "liver",  "bone", "brain", 
        "bone", "brain", "brain", "bone",  "lung",  "lung", 
        "lung", "liver", "bone", "lung", "lung")
gr1 <- paste0(gr, seq_along(gr))
###ex <- subset(ex, select = -c(brain18, brain8, lung36, lung30, lung1, lung2, lung17, liver7, liver14, liver27, bone25, bone19, bone12))
colnames(ex) <- gr1


library(ggplot2)
PCR <- data.frame(pc$r[, 1:2], Group = gr)
pdf("~/Documents/Bioinformatics - R/Results/PCR modified.pdf", width = 10, height= 8)
ggplot (PCR,aes(PC1, PC2, color = gr)) + geom_point(size = 3) + theme_bw()
ggplot (PCR,aes(PC1, PC2, label = gr1)) + geom_text(size = 3) + theme_bw()
dev.off()



###defrential expression analysis
gr <- factor(gr)
mat = data.frame(G=gr)
rownames(mat) <- colnames(ex)
design = model.matrix(~G+0 , mat)
colnames(design) <- levels(gr)
fit <- lmFit(ex,design)
cont.matrix <- makeContrasts (contrasts = "bone-lung" , levels = design)
fit2 <- contrasts.fit (fit, cont.matrix)
fit2 <- eBayes (fit2, 0.01)
tT = topTable(fit2, adjust = "fdr", sort.by = "B" , number = Inf)


Up   <- subset(tT, logFC >  1 & P.Value < 0.5)
Down <- subset(tT, logFC < -1 & P.Value < 0.5)

dim(Up)
dim(Down)


install.packages('car')
Export(tT, 'tT.xlsx')
dev.off()

