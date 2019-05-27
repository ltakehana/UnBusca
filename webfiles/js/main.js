
function addTag(){
	if($("#SearchField").val()!=""){
		if($("#TagsFilters").val()==""){
			$("#TagsFilters").val($("#SearchField").val());
		}
		else{
			$("#TagsFilters").val($("#TagsFilters").val()+"[,]"+$("#SearchField").val());
		}
		$("#TagsNames").append(" <label onclick=\"delTag('"+$("#SearchField").val()+"')\" class=\"filtro\">"+$("#SearchField").val()+" &nbsp;&nbsp;<span style=\"font-weight:1\">x</span></label>");
		$("#SearchField").val("");
	}
}

function insertTag(Tag){
	if(Tag!=""){
		Tag=(String(Tag))
		if($("#TagsFilters").val()==""){
			$("#TagsFilters").val(Tag);
		}
		else{
			$("#TagsFilters").val($("#TagsFilters").val()+"[,]"+Tag);
		}
		$("#TagsNames").append(" <label onclick=\"delTag('"+Tag+"')\" class=\"filtro\">"+Tag+" &nbsp;&nbsp;<span style=\"font-weight:1\">x</span></label>");
	}
}
function delTag(Tag){
	var Tags=$("#TagsNames").html()
	var remover=" <label onclick=\"delTag('"+Tag+"')\" class=\"filtro\">"+Tag+" &nbsp;&nbsp;<span style=\"font-weight:1\">x</span></label>";
	Tags=(Tags.replace(remover,""));
	$("#TagsNames").html(Tags)
	Tags=$("#TagsFilters").val()
	remover=Tags.replace(Tag+"[,]","");
	if(Tags != remover){
		$("#TagsFilters").val(remover)
	}
	else {
		remover=Tags.replace("[,]"+Tag,"");
		if(Tags != remover){
			$("#TagsFilters").val(remover)
		}
		else{
			remover=Tags.replace(Tag,"");
			$("#TagsFilters").val(remover)
		}
	}
}

function alterarLocal(local){
	$("#localPost").val(local);
	$("#btnGroupDrop1").text(local);
}
