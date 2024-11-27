from fastapi import APIRouter, Form, Path, Query, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.categoria_model import CategoriaModel
from models.produto_model import ProdutoModel
from repos.categoria_repo import CategoriaRepo
from repos.produto_repo import ProdutoRepo
from util.mensagens import *


router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_root(request: Request):
    produtos = ProdutoRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/index.html", {"request": request, "produtos": produtos})
    return response


# Categoria

@router.get("/lista_categorias")
def get_listar_categorias(request: Request):
    lista_categorias = CategoriaRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/lista_categorias.html", {"request": request, "lista_categorias": lista_categorias})
    return response


@router.get("/alterar_categoria/{id}")
def get_alterar_categoria(request: Request, id: int = Path(...)):
    categoria = CategoriaRepo.obter_por_id(id)
    response = templates.TemplateResponse(
        "admin/alterar_categoria.html", {"request": request, "categoria": categoria}
        )
    return response

@router.post("/alterar_categoria/{id}")
def post_alterar_categoria(
    request: Request, 
    id: int = Path(...),
    nome: str = Form(...)):
    categoria = CategoriaModel(id, nome)
    if CategoriaRepo.alterar(categoria):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Categoria alterada com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/alterar_categoria.html", {"request": request, "categoria": categoria})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response

@router.get("/inserir_categoria")
def get_inserir_categoria(request: Request):
    categoria = CategoriaModel(None, None)
    response = templates.TemplateResponse(
        "admin/inserir_categoria.html", {"request": request, "categoria": categoria}
    )
    return response

@router.post("/inserir_categoria")
def post_inserir_categoria(
    request: Request,
    nome: str = Form(...)):
    categoria = CategoriaModel(None, nome)
    if CategoriaRepo.inserir(categoria):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Categoria inserida com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/inserir_categoria.html", {"request": request, "categoria": categoria})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.get("/excluir_categoria/{id}")
def get_excluir_categoria(request: Request, id: int = Path(...)):
    categoria = CategoriaRepo.obter_por_id(id)
    if categoria:
        response = templates.TemplateResponse(
            "admin/excluir_categoria.html", {"request": request, "categoria": categoria}
        )
        return response
    else:
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_erro(response, "O categoria que você tentou excluir não existe!")
        return response
    
@router.post("/excluir_categoria")
def post_excluir_categoria(id: int = Form(...)):
    if CategoriaRepo.excluir(id):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Categoria excluída com sucesso!")
        return response
    else:
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_erro(response, "Não foi possível excluir a categoria!")
        return response


# Produto

@router.get("/alterar_produto/{id}")
def get_alterar_produto(request: Request, id: int = Path(...)):
    produto = ProdutoRepo.obter_por_id(id)
    lista_categorias = CategoriaRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/alterar_produto.html", {"request": request, "produto": produto, "lista_categorias": lista_categorias}
        )
    return response

@router.post("/alterar_produto/{id}")
def post_alterar_produto(
    request: Request, 
    id: int = Path(...),
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...),
    categoria: int = Form(...)):
    produto = ProdutoModel(id, nome, descricao, preco, estoque, categoria)
    if ProdutoRepo.alterar(produto):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Produto alterado com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/alterar_produto.html", {"request": request, "produto": produto})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response

@router.get("/inserir_produto")
def get_inserir_produto(request: Request):
    produto = ProdutoModel(None, None, None, None, None)
    lista_categorias = CategoriaRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/inserir_produto.html", {"request": request, "produto": produto, "lista_categorias": lista_categorias}
    )
    return response

@router.post("/inserir_produto")
def post_inserir_produto(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...),
    categoria: int = Form(...)):
    produto = ProdutoModel(None, nome, descricao, preco, estoque, categoria)
    if ProdutoRepo.inserir(produto):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Produto inserido com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/inserir_produto.html", {"request": request, "produto": produto})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.get("/excluir_produto/{id}")
def get_excluir_produto(request: Request, id: int = Path(...)):
    produto = ProdutoRepo.obter_por_id(id)
    if produto:
        response = templates.TemplateResponse(
            "admin/excluir_produto.html", {"request": request, "produto": produto}
        )
        return response
    else:
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_erro(response, "O produto que você tentou excluir não existe!")
        return response
    
@router.post("/excluir_produto")
def post_excluir_produto(id: int = Form(...)):
    if ProdutoRepo.excluir(id):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Produto excluído com sucesso!")
        return response
    else:
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_erro(response, "Não foi possível excluir o produto!")
        return response