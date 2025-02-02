function buscarEndereco() {
    const cep = document.querySelector('input[name="cep"]').value;
    if (cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    document.querySelector('input[name="logradouro"]').value = data.logradouro;
                    document.querySelector('input[name="bairro"]').value = data.bairro;
                    document.querySelector('input[name="cidade"]').value = data.localidade;
                    document.querySelector('input[name="estado"]').value = data.uf;
                } else {
                    alert('CEP não encontrado!');
                }
            })
            .catch(error => {
                alert('Erro ao buscar CEP!');
                console.error('Erro:', error);
            });
    }
}

document.getElementById('corretorForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('confirmationMessage').style.display = 'block';
            form.reset();
            atualizarTabela();
        } else {
            alert('Erro ao cadastrar corretor!');
        }
    })
    .catch(error => {
        alert('Erro ao cadastrar corretor!');
        console.error('Erro:', error);
    });
});

function atualizarTabela() {
    fetch('/get_corretores')
        .then(response => response.json())
        .then(data => {
            const tabela = document.getElementById('corretoresTable');
            tabela.innerHTML = '';
            data.forEach(corretor => {
                const row = tabela.insertRow();
                row.innerHTML = `
                    <td>${corretor.cpf}</td>
                    <td>${corretor.nome_completo}</td>
                    <td>${corretor.data_nascimento}</td>
                    <td>${corretor.imobiliaria}</td>
                    <td>${corretor.creci}</td>
                    <td>${corretor.estado_creci}</td>
                    <td>${corretor.telefone}</td>
                    <td>${corretor.email}</td>
                    <td>${corretor.cep}</td>
                    <td>${corretor.logradouro}</td>
                    <td>${corretor.bairro}</td>
                    <td>${corretor.cidade}</td>
                    <td>${corretor.estado}</td>
                    <td>${corretor.numero}</td>
                    <td>
                        <button class="btn btn-warning btn-sm" onclick="editarCorretor(${corretor.id})">Editar</button>
                        <button class="btn btn-danger btn-sm" onclick="deletarCorretor(${corretor.id})">Deletar</button>
                    </td>
                `;
            });
        })
        .catch(error => {
            console.error('Erro ao atualizar tabela:', error);
        });
}

function editarCorretor(id) {
    fetch(`/get_corretor/${id}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('corretorId').value = data.id;
            document.getElementById('cpf').value = data.cpf;
            document.getElementById('nome_completo').value = data.nome_completo;
            document.getElementById('data_nascimento').value = data.data_nascimento.split('-').reverse().join('-'); // Formato brasileiro
            document.getElementById('imobiliaria').value = data.imobiliaria;
            document.getElementById('creci').value = data.creci;
            document.getElementById('estado_creci').value = data.estado_creci;
            document.getElementById('telefone').value = data.telefone;
            document.getElementById('email').value = data.email;
            document.getElementById('cep').value = data.cep;
            document.getElementById('logradouro').value = data.logradouro;
            document.getElementById('bairro').value = data.bairro;
            document.getElementById('cidade').value = data.cidade;
            document.getElementById('estado').value = data.estado;
            document.getElementById('numero').value = data.numero;

            document.querySelector('button[type="submit"]').style.display = 'none';
            document.getElementById('salvarAlteracoes').style.display = 'inline-block';
        })
        .catch(error => {
            console.error('Erro ao buscar corretor:', error);
        });
}

function salvarAlteracoes() {
    const form = document.getElementById('corretorForm');
    const formData = new FormData(form);

    fetch(`/update_corretor/${formData.get('id')}`, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('confirmationMessage').style.display = 'block';
            form.reset();
            document.querySelector('button[type="submit"]').style.display = 'inline-block';
            document.getElementById('salvarAlteracoes').style.display = 'none';
            atualizarTabela();
        } else {
            alert('Erro ao salvar alterações!');
        }
    })
    .catch(error => {
        alert('Erro ao salvar alterações!');
        console.error('Erro:', error);
    });
}

function deletarCorretor(id) {
    fetch(`/delete_corretor/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            atualizarTabela();
        } else {
            alert('Erro ao deletar corretor!');
        }
    })
    .catch(error => {
        alert('Erro ao deletar corretor!');
        console.error('Erro:', error);
    });
}

document.addEventListener('DOMContentLoaded', atualizarTabela);