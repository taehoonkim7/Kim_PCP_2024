import sys


def Make_gene_lst (f_in):

    gene_lst = []
    with open (f_in, 'r') as f:
        for l in f:
            gene_lst.append (l.strip())

    return gene_lst


def Filter_syn (gene_lst, f_syn):

    syn_lst = []
    with open (f_syn, 'r') as f:
        for l in f:
            l = l.strip()
            *_, query, subject = l.split('\t')
            if (query in gene_lst) and (subject in gene_lst):
                syn_lst.append (l)

    return syn_lst


def Print_lst (syn_lst, f_o):

    o = open (f_o, 'w')
    print ("block_id\tblock_score\tgene1\tgene2", file = o)

    for l in syn_lst:
        print (l, file = o)
    
    o.close()


def main ():
    f_gene  = sys.argv[1]
    f_syn   = sys.argv[2]
    f_o     = sys.argv[3]

    gene_lst = Make_gene_lst(f_gene)
    syn_lst  = Filter_syn(gene_lst, f_syn)
    Print_lst (syn_lst, f_o)


if __name__ == "__main__":
    main()
