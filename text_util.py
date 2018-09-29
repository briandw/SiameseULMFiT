re1 = re.compile(r'  +')

def fixup_string(x):
    x = x.replace('#39;', "'").replace('amp;', '&').replace('#146;', "'").replace(
        'nbsp;', ' ').replace('#36;', '$').replace('\\n', "\n").replace('quot;', "'").replace(
        '<br />', "\n").replace('\\"', '"').replace('<unk>','u_n').replace(' @.@ ','.').replace(
        ' @-@ ','-').replace('\\', ' \\ ')
    return re1.sub(' ', html.unescape(x))

def get_texts(df):
    texts = df[0].astype(str)
    texts = list(texts.apply(fixup).values)
    texts = f'x_bos ' + df[0].astype(str)
    tok = Tokenizer().proc_all_mp(partition_by_cores(texts))
    return tok