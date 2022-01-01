setwd("~/Documents/Bioinformatics - R/RNAseq")

cn <- read.delim()

###prepration###

cn <- subset(cn, select = c(-ensembl))
rownames(cn) <- cn$hgnc_symbol
cn <- cn[!duplicated(cn$hgnc_symbol)]
cn <- subset(cn, select = -hgnc_symbol)


write.table(cn, "cont.txt",row.names = T, col.names = F, sep= "\t")


gr <- c(rep("Barain-m", 3), rep("Lung-M", 3), rep("Normal", 3))
grt <- paste0(gr, ".", seq(ncol(cn)))

colnames(cn) <- gr


####quality control

setwd("~/Documents/Bioinformatics - R/RNAseq/Result")
w <- data.frame(cnt)
w <- subset(w, select = c(-lung-M.4))


grt <- c("Barain-m.1", "Barain-m.2", "Barain-m.3",
         "Lung-M.4", "Lung-M.5", "Lung-M.6",
         "Normal.7", "Normal.8", "Normal.9")
pdf("~/Documents/Bioinformatics - R/RNAseq/Result/Boxplot.pdf", width = 15, height = 15)
boxplot(W)
dev.off()


pdf("~/Documents/Bioinformatics - R/RNAseq/Result/PCdrid.pdf", width = 15, height = 15)
pc <- prcomp(w)
ex.scale <- t(scale(t(w), scale = F))
pc1  <- prcomp(ex.scale)
pcr  <- data.frame(pc1$r[, 1:3], Group = gr)
pcrt <- data.frame(pc1$r[, 1:3], Group = grT)

p1 <- ggplot(pcr, aes(PC1, PC2, color = Group)) +geom_point(size=5)+ theme_bw(basesize = 15)
p2 <- ggplot(pcr, aes(PC1, PC2, lable = Group)) +geom_point(size=5)+ theme_bw(basesize = 10)
grid.arrange(p1, p2, nrow = 2)
dev.off()


#deffrentian expression

gr <- as.factor(gr)
coldata <- data.frame(group = gr, type = "singel-end")
cds <- DESeqDataSetFormMatrix(cn, colData, design = ~group)
cds <- DESeq(cds)
cnt <- log2(1+counts(cds, normalize = T))

dif <- data.frame(results(cds, c("group", "Normal", "Brain-M")))
dif$padj <- p.adjust(dif$pvalue, method = "BH")
dif <- dif[order(dif$padj),]
pdf("Brain-Valcanoplot.pdf")
ggplot(dif, aes(log2FoldChange, -log10(pvalue), color = log2FoldChange)) + geom_piont() + theme_bw

till.up <- subset(dif, log2FoldChange > 1 & pvalue < 0.05)
till.up$gene <- rownames(till.up)
till.down <- subset(dif, log2FoldChange < -1 & pvalue < 0.05) 
till.down$gene <- row(till.down)
write.table(cnt, "cnt.txt" , qoute = F, row.names = T, sep = "\t")
 
 
setwd("Brain/")
write.table (dif, "DEGs_Brain_vs_Normal.txt", qoute = F, row.names = T, sep = "\t" )
write.table (cn, "Counts_Brain_vs_Normal.txt", qoute = F, row.names = T, sep = "\t" )
write.table (till.up, "upregulated_Brain_vs_Normal.txt", qoute = F, row.names = F, sep = "\t" )
write.table (till.down, "downregulated_Brain_vs_Normal.txt", qoute = F, row.names = F, sep = "\t" )
write.table (till.up$gene, "1420up_Brain_vs_Normal.txt", qoute = F, row.names = F, sep = "\t" )
write.table (till.down$gene, "1420down_Brain_vs_Normal.txt", qoute = F, row.names = F, sep = "\t" )







