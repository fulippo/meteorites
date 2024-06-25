# Default labels helper
{{- define "db.defaultLabels" -}}
app.kubernetes.io/component: database
app.kubernetes.io/name: {{ .Values.name }}
app.kubernetes.io/version: {{ .Chart.Version }}
app: {{ .Values.name }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
tier: mysql
{{- end }}