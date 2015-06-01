#改进1,用mp3lame替换pcm编码
mencoder -forceidx -of lavf -oac mp3lame -ovc copy -o output.flv 1.flv 2.flv 3.flv

#这种方式产生的文件比用pcm方式小了很多，大概比原来的总文件大小大50%左右，可以接受，但仍然不太完美。

#改进2,用mp3lame替换pcm编码，并指定码率（待实验）
mencoder -forceidx -of lavf -oac mp3lame -lameopts abr:br=24 -ovc copy -o output.flv 1.flv 2.flv 3.flv

#改进3 用faac编码也可以使合并后的文件与原来的文件差不多大（待实验）
mencoder -oac faac -ovc copy -idx -o output1.flv 1.flv 2.flv 3.flv 