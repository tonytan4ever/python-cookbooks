from jinja2 import Template


upsert_tpl_string = '''
begin;
create temp table {{ table_name }}_clone as select * from {{ table_name }} with no data;
\copy {{ table_name }}_clone FROM '{{ csv_dump_path }}' delimiter ',' csv header;
insert into {{ table_name }} select  * from {{ table_name }}_clone on conflict do nothing;
commit;
'''

dump_csv_string = '''
    \copy {{ table_name }} TO '{{ csv_dump_path }}' delimiter ',' csv header;
'''

set_table_max_id_seq_string = '''
    select setval('{{ table_name }}_id_seq', (select MAX(id) from {{ table_name }));
'''

def get_upsert_transaction(table_name, csv_dump_path):
    return Template(upsert_tpl_string).render(
        table_name = table_name,
        csv_dump_path = csv_dump_path
    )


def get_dump_csv_stmt(table_name, csv_dump_path):
    return Template(dump_csv_string).render(
        table_name = table_name,
        csv_dump_path = csv_dump_path
    )
    
def get_set_table_max_id_seq_stmt(table_name):
    return Template(set_table_max_id_seq_string).render(
        table_name = table_name
    )