insert into department (name)
values
    ('college of computing'),
    ('college of design'),
    ('college of engineering'),
    ('college of sciences'),
    ('ivan allen college of liberal arts'),
    ('scheller college of business')
;

insert into major (name, department_name)
values
    ('computational media', 'college of computing'),
    ('computer science', 'college of computing'),
    ('architecture', 'college of design'),
    ('industrial design', 'college of design'),
    ('music technology', 'college of design'),
    ('aerospace engineering', 'college of engineering'),
    ('biomedical engineering', 'college of engineering'),
    ('chemical and biomolecular engineering', 'college of engineering'),
    ('civil engineering', 'college of engineering'),
    ('computer engineering', 'college of engineering'),
    ('electrical engineering', 'college of engineering'),
    ('environmental engineering', 'college of engineering'),
    ('industrial engineering', 'college of engineering'),
    ('materials science and engineering', 'college of engineering'),
    ('mechanical engineering', 'college of engineering'),
    ('nuclear and radiological engineering', 'college of engineering'),
    ('applied mathematics', 'college of sciences'),
    ('applied physics', 'college of sciences'),
    ('biochemistry', 'college of sciences'),
    ('biology', 'college of sciences'),
    ('chemistry', 'college of sciences'),
    ('discrete mathematics', 'college of sciences'),
    ('earth and atmospheric sciences', 'college of sciences'),
    ('physics', 'college of sciences'),
    ('psychology', 'college of sciences'),
    ('applied language and intercultural studies', 'ivan allen college of liberal arts'),
    -- ('computational media', 'ivan allen college of liberal arts'),
    ('economics', 'ivan allen college of liberal arts'),
    ('economics and international affairs', 'ivan allen college of liberal arts'),
    ('global economics and modern languages', 'ivan allen college of liberal arts'),
    ('history, technology, and society', 'ivan allen college of liberal arts'),
    ('international affairs', 'ivan allen college of liberal arts'),
    ('international affairs and modern languages', 'ivan allen college of liberal arts'),
    ('literature, media, and communication', 'ivan allen college of liberal arts'),
    ('public policy', 'ivan allen college of liberal arts'),
    ('business administration', 'scheller college of business')
;
