import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False, 'Preço': ':.2f'},
    title='Receita por Estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mes',
    y='Preço',
    markers=True,
    range_y = (0, df_rec_mensal.max()),
    color='Ano',
    line_dash = 'Ano',
    title = 'Receita Mensal'
)

grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

grafico_rec_estado = px.bar(
    df_rec_estado.head(7),
    x='Local da compra',
    y='Preço',
    text_auto = True,
    # color='Local da compra',
    title='Top Receita por Estado'
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto = True,
    title='Top 7 Categorias com Maior Receita'
    # x='Categoria do Produto',
    # y='Preço',
    # color='Local da compra',
)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 Vendedores com Maior Receita'
)

grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 Vendedores com Maior Número de Vendas',
)

df_vendedores["ticket_medio"] = df_vendedores["sum"] / df_vendedores["count"]
print(df_vendedores)

grafico_ticket_medio = px.bar(
    df_vendedores[['ticket_medio']].sort_values('ticket_medio', ascending=False).head(7),
    x = 'ticket_medio',
    y = df_vendedores[['ticket_medio']].sort_values('ticket_medio', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 Vendedores com Maior Ticket Médio',
)