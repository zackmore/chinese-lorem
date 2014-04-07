# Chinese Lorem Ipsum

类似于 [lipsum](http://www.lipsum.com)，这是中文伪文生成器，适用于生成中文验证码、填充文本、以及装疯卖傻。

## Usage

-   `python ipsum.py -h` 查看帮助信息
-   `python ipsum.py -n <number>` 生成的个数（整数类型。默认为 **1**）
-   `python ipsum.py -t <type>` 生成的类型（`c`：字，`w`：词，`s`：句，`p`：段落。默认为 **p**）
-   `python ipsum.py -z <meaning_flag>` 生成的文本是否常见（`1`：常见，`0`：不常见。默认为 **1**）